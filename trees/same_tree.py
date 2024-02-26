#QUESTION:

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# eg:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# eg:
# p=[1,1], q=[1,null,1] , output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #this is faster
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif not p and q:
            return False
        
        if p and q:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        #bfs
        # q1=[]
        # q2=[]
        
        # if not p and not q:
        #     return True
        # if p and not q:
        #     return False
        # if q and not p:
        #     return False
        
        # q1.append(p)
        # q2.append(q)

        # while q1 and q2:
        #     root1=q1.pop(0)
        #     root2=q2.pop(0)

        #     if root1.val!=root2.val:
        #         return False

        #     if (root1.left and not root2.left) or \
        #     (root1.right and not root2.right) or \
        #     (not root1.left and root2.left) or \
        #     (not root1.right and root2.right):
        #         return False
        #     if root1.left :
        #         q1.append(root1.left)
        #         q2.append(root2.left)
        #     if root1.right:
        #         q1.append(root1.right)
        #         q2.append(root2.right)
        # return True
            
        #checking inorder or any of the tree traversals will not work
        #because p=[1,1], q=[1,null,1] will fail
        
        # return self.inorder(p)==self.inorder(q) and self.preorder(p)==self.preorder(q)
        
        
    
    # def inorder(self,root):
    #     res=[]
    #     if root:
    #         res+=self.inorder(root.left)
    #         res.append(root.val)
    #         res+=self.inorder(root.right)
    #     return res
    
    # def preorder(self,root):
    #     res=[]
    #     if root:
    #         res.append(root.val)
    #         res+=self.preorder(root.left)
    #         res+=self.preorder(root.right)
    #     return res


        