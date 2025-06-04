class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution(object):
    def __init__(self):
        self.max_depth = 0
        

    def maxDepth(self, root):
        actual_depth = 0
        def deeper(root, actual_depth):
            if not root:
                return 0
            actual_depth +=1
            if actual_depth > self.max_depth:
                self.max_depth = actual_depth
            
            deeper(root.left, actual_depth)
            deeper(root.right, actual_depth)

            return self.max_depth

        return deeper(root, actual_depth)

            

tree = Node(5,
            Node(4,
                 Node(11, Node(7), Node(2))),
            Node(8,
                 Node(13),
                 Node(4, None, Node(1))))

sol = Solution()
print(sol.isSymmetric(tree))
