import os
import shutil
import tempfile
import logging
from pathlib import Path
from unittest import mock
import pytest

from sync import FolderSynchronizer, setup_logger


@pytest.fixture
def temp_dirs():
    with (
        tempfile.TemporaryDirectory() as source_dir,
        tempfile.TemporaryDirectory() as replica_dir,
    ):
        yield Path(source_dir), Path(replica_dir)


@pytest.fixture
def logger():
    return setup_logger(log_file=os.devnull)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        f.write(content)


def read_file(path: Path) -> str:
    with path.open("r") as f:
        return f.read()


def test_copy_new_file(temp_dirs: tuple[Path, Path], logger: logging.Logger) -> None:
    source, replica = temp_dirs
    file_path = source / "file.txt"
    write_file(file_path, "hello")

    sync = FolderSynchronizer(source, replica, logger)
    sync.synchronize()

    assert (replica / "file.txt").exists()
    assert read_file(replica / "file.txt") == "hello"


def test_update_changed_file(
    temp_dirs: tuple[Path, Path], logger: logging.Logger
) -> None:
    source, replica = temp_dirs
    write_file(source / "file.txt", "new content")
    write_file(replica / "file.txt", "old content")

    sync = FolderSynchronizer(source, replica, logger)
    sync.synchronize()

    assert read_file(replica / "file.txt") == "new content"


def test_delete_extra_file(
    temp_dirs: tuple[Path, Path], logger: logging.Logger
) -> None:
    source, replica = temp_dirs
    write_file(replica / "obsolete.txt", "bye")

    sync = FolderSynchronizer(source, replica, logger)
    sync.synchronize()

    assert not (replica / "obsolete.txt").exists()


def test_create_directory_structure(
    temp_dirs: tuple[Path, Path], logger: logging.Logger
) -> None:
    source, replica = temp_dirs
    write_file(source / "a/b/c.txt", "nested")

    sync = FolderSynchronizer(source, replica, logger)
    sync.synchronize()

    assert (replica / "a/b/c.txt").exists()
    assert read_file(replica / "a/b/c.txt") == "nested"


def test_remove_extra_directory(
    temp_dirs: tuple[Path, Path], logger: logging.Logger
) -> None:
    source, replica = temp_dirs
    (replica / "extra_dir").mkdir()
    write_file(replica / "extra_dir/file.txt", "bye")
    os.remove(replica / "extra_dir/file.txt")  # So dir can be removed

    sync = FolderSynchronizer(source, replica, logger)
    sync.synchronize()

    assert not (replica / "extra_dir").exists()


def test_symlink_file(temp_dirs: tuple[Path, Path], logger: logging.Logger) -> None:
    source, replica = temp_dirs
    target = source / "target.txt"
    write_file(target, "real")
    symlink = source / "link.txt"
    symlink.symlink_to(target)

    sync = FolderSynchronizer(source, replica, logger)
    sync.synchronize()

    assert (replica / "link.txt").is_symlink()
    assert os.readlink(replica / "link.txt") == str(target)


def test_symlink_directory(
    temp_dirs: tuple[Path, Path], logger: logging.Logger
) -> None:
    source, replica = temp_dirs
    target_dir = source / "real_dir"
    target_dir.mkdir()
    (target_dir / "f.txt").write_text("inside")
    symlink = source / "link_dir"
    symlink.symlink_to(target_dir, target_is_directory=True)

    sync = FolderSynchronizer(source, replica, logger)
    sync.synchronize()

    assert (replica / "link_dir").is_symlink()
    assert os.readlink(replica / "link_dir") == str(target_dir)


def test_partial_copy_fails_and_logs(
    temp_dirs: tuple[Path, Path], logger: logging.Logger, caplog: mock.MagicMock
) -> None:
    source, replica = temp_dirs
    file = source / "file.txt"
    write_file(file, "data")

    # Simulate _sha256 returning different hash to trigger retries
    sync = FolderSynchronizer(source, replica, logger)
    original_sha256 = sync._sha256

    counter = {"calls": 0}

    def inconsistent_sha256(file_path):
        counter["calls"] += 1
        return str(counter["calls"])  # Different every time to simulate file changing

    sync._sha256 = inconsistent_sha256
    sync._safe_copy(file, replica / "file.txt")

    sync._sha256 = original_sha256  # Restore

    assert counter["calls"] > 3
    assert "Failed to copy consistent version" in caplog.text


def test_permission_error_on_delete(
    temp_dirs: tuple[Path, Path], logger: logging.Logger, caplog: mock.MagicMock
) -> None:
    source, replica = temp_dirs
    file = replica / "file.txt"
    write_file(file, "cannot delete")

    with mock.patch("pathlib.Path.unlink", side_effect=PermissionError("no access")):
        sync = FolderSynchronizer(source, replica, logger)
        sync.synchronize()

    assert "Permission denied deleting file" in caplog.text


def test_permission_error_on_copy(
    temp_dirs: tuple[Path, Path], logger: logging.Logger, caplog: mock.MagicMock
) -> None:
    source, replica = temp_dirs
    file = source / "file.txt"
    write_file(file, "some data")

    with mock.patch("shutil.copy2", side_effect=PermissionError("no access")):
        sync = FolderSynchronizer(source, replica, logger)
        sync.synchronize()

    assert "Permission denied copying file" in caplog.text


def test_error_on_reading_symlink(
    temp_dirs: tuple[Path, Path], logger: logging.Logger, caplog: mock.MagicMock
) -> None:
    source, replica = temp_dirs
    bad_symlink = source / "bad_link"
    bad_symlink.symlink_to("nonexistent_target")

    sync = FolderSynchronizer(source, replica, logger)
    with mock.patch("os.readlink", side_effect=OSError("broken")):
        sync.synchronize()

    assert "Unexpected error during synchronization: broken" in caplog.text
