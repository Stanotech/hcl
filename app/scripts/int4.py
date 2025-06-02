class Node:

    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def check_sum(self, root, target_sum, sum):         
        if root == None:
            return False
        
        sum += root.val

        if root.left == None and root.right == None:
            if sum == target_sum:
                return True

        return self.check_sum(root.left, target_sum, sum) or self.check_sum(root.right, target_sum, sum)


tree = Node(5,
            Node(4,
                 Node(11, Node(7), Node(2))),
            Node(8,
                 Node(13),
                 Node(4, None, Node(1))))

sum = 0
sol = Solution()
print(sol.check_sum(tree, 22, sum))  # True
print(sol.check_sum(tree, 26, sum))  # True (5->8->13)
print(sol.check_sum(tree, 100, sum)) # False
