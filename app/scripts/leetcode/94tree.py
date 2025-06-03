class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def __init__(self):
        self.result = []

    def inorder(self, root):        
        if root is None:
            return []

        self.inorder(root.left)
        self.result.append(root.val) 
        self.inorder(root.right)

        return self.result

            

tree = Node(5,
            Node(4,
                 Node(11, Node(7), Node(2))),
            Node(8,
                 Node(13),
                 Node(4, None, Node(1))))

sol = Solution()
print(sol.inorder(tree))
