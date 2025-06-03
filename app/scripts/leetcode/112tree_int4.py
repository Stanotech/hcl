class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def check_sum(self, root, target_sum, current_sum=0):         
        if root is None:
            return False
        
        current_sum += root.val

        if root.left is None and root.right is None:
            return current_sum == target_sum

        return (
            self.check_sum(root.left, target_sum, current_sum) or
            self.check_sum(root.right, target_sum, current_sum)
        )

tree = Node(5,
            Node(4,
                 Node(11, Node(7), Node(2))),
            Node(8,
                 Node(13),
                 Node(4, None, Node(1))))

sol = Solution()
print(sol.check_sum(tree, 22))  # True
print(sol.check_sum(tree, 26))  # True
print(sol.check_sum(tree, 100)) # False