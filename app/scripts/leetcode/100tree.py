class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            pass
        
        else:
            if (p == None and q != None) or (q == None and p != None):
                return False

            if p.val != q.val:
                return False        
            
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return True

            

tree = Node(5,
            Node(4,
                 Node(11, Node(7), Node(2))),
            Node(8,
                 Node(13),
                 Node(4, None, Node(1))))

sol = Solution()
print(sol.inorder(tree))
