import os
import shutil
import hashlib
import time
import logging
import sys
from pathlib import Path
from typing import Optional


class FolderSynchronizer:
    def __init__(self, source: Path, replica: Path, logger: logging.Logger):
        self.source = source
        self.replica = replica
        self.logger = logger

    def synchronize(self):
        try:
            self._delete_removed_files()    # Delete first to prevent conflict between folder and file with the same name
            self._ensure_replica_exists()
            self._copy_and_update_files()
        except (KeyboardInterrupt, SystemExit):
            self.logger.error("Critical interruption during synchronization. Propagating exception.")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during synchronization: {e}")

    def _ensure_replica_exists(self):
        if not self.replica.exists():
            self.replica.mkdir(parents=True)
            self.logger.info(f"Created replica folder: {self.replica}")

    def _copy_and_update_files(self):
        for root, dirs, files in os.walk(self.source):
            rel_root = Path(root).relative_to(self.source)
            replica_root = self.replica / rel_root

            self._sync_directories(dirs, replica_root, Path(root))
            self._sync_files(files, replica_root, Path(root))

    def _sync_directories(self, dirs, replica_root: Path, source_root: Path):
        for dir_name in dirs:
            source_dir = source_root / dir_name
            target_dir = replica_root / dir_name

            if source_dir.is_symlink():
                link_target = os.readlink(source_dir)
                if target_dir.exists() or target_dir.is_symlink():
                    target_dir.unlink()
                target_dir.parent.mkdir(parents=True, exist_ok=True)
                os.symlink(link_target, target_dir)
                self.logger.info(f"Created symlink directory: {target_dir} -> {link_target}")
                continue
            elif not target_dir.exists():
                target_dir.mkdir(parents=True)
                self.logger.info(f"Created directory: {target_dir}")

    def _sync_files(self, files, replica_root: Path, source_root: Path):
        for file_name in files:
            source_file = source_root / file_name
            replica_file = replica_root / file_name

            if source_file.is_symlink():
                link_target = os.readlink(source_file)
                if replica_file.exists() or replica_file.is_symlink():
                    replica_file.unlink()
                replica_file.parent.mkdir(parents=True, exist_ok=True)
                os.symlink(link_target, replica_file)
                self.logger.info(f"Created symlink file: {replica_file} -> {link_target}")
                continue
            elif not replica_file.exists():
                self._safe_copy(source_file, replica_file)
                self.logger.info(f"Copied new file: {replica_file}")
            elif self._files_differ(source_file, replica_file):
                self._safe_copy(source_file, replica_file)
                self.logger.info(f"Updated file: {replica_file}")

    def _delete_removed_files(self):
        for root, dirs, files in os.walk(self.replica, topdown=False):
            rel_root = Path(root).relative_to(self.replica)
            source_root = self.source / rel_root

            # Delete files not in source
            for file_name in files:
                replica_file = Path(root) / file_name
                source_file = source_root / file_name
                if not source_file.exists():
                    try:
                        replica_file.unlink()
                        self.logger.info(f"Deleted file: {replica_file}")
                    except PermissionError as e:
                        self.logger.error(f"Permission denied deleting file {replica_file}: {e}")
                    except Exception as e:
                        self.logger.warning(f"Failed to delete file {replica_file}: {e}")

            # Delete empty directories not in source
            for dir_name in dirs:
                replica_dir = Path(root) / dir_name
                source_dir = source_root / dir_name
                if not source_dir.exists() and not any(replica_dir.iterdir()):
                    try:
                        replica_dir.rmdir()
                        self.logger.info(f"Deleted directory: {replica_dir}")
                    except PermissionError as e:
                        self.logger.error(f"Permission denied deleting directory {replica_dir}: {e}")
                    except Exception as e:
                        self.logger.warning(f"Failed to delete directory {replica_dir}: {e}")

    def _safe_copy(self, source: Path, target: Path, retries: int = 3):
        for attempt in range(retries):
            try:
                source_hash_before = self._md5(source)
                shutil.copy2(source, target)
                target_hash = self._md5(target)
                source_hash_after = self._md5(source)

                if source_hash_before == source_hash_after == target_hash:
                    return
                self.logger.warning(f"Source file changed during copy: {source}. Retrying ({attempt + 1}/{retries})")
            except PermissionError as e:
                self.logger.error(f"Permission denied copying file {source} to {target}: {e}")
                break
            except Exception as e:
                self.logger.error(f"Error copying file {source} to {target}: {e}")
        self.logger.error(f"Failed to copy consistent version of file after {retries} attempts: {source}")

    def _files_differ(self, file1: Path, file2: Path) -> bool:
        return self._md5(file1) != self._md5(file2)

    def _md5(self, file_path: Path) -> Optional[str]:
        hash_md5 = hashlib.md5()
        try:
            with file_path.open("rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return None

def setup_logger(log_file: str) -> logging.Logger:
    logger = logging.getLogger("FolderSynchronizer")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def main():
    if len(sys.argv) != 6:
        print("Usage: python sync.py <source_folder> <replica_folder> <interval_seconds> <sync_count> <log_file>")
        return

    source_path = Path(sys.argv[1]).resolve()
    replica_path = Path(sys.argv[2]).resolve()
    try:
        interval = int(sys.argv[3])
        repetitions = int(sys.argv[4])
        if interval <= 0 or repetitions <= 0:
            print("Error: interval and sync_count must be positive integers.")
            return
    except ValueError:
        print("Interval and sync_count must be integers.")
        return

    log_file = sys.argv[5]
    logger = setup_logger(log_file)

    if not source_path.exists() or not source_path.is_dir():
        logger.error(f"Source folder does not exist or is not a directory: {source_path}")
        return

    synchronizer = FolderSynchronizer(source_path, replica_path, logger)

    for i in range(repetitions):
        logger.info(f"--- Synchronization {i + 1}/{repetitions} ---")
        synchronizer.synchronize()
        if i < repetitions - 1:
            time.sleep(interval)

if __name__ == "__main__":
    main()
