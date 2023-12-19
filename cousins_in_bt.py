#question : Cousins in Binary Tree

#https://leetcode.com/problems/cousins-in-binary-tree/

#Algo:
# Check the depth and parent of the given nodes.
# Cousins in a binary tree have same depth but diff parents.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        #cousins have same depth and diff parents
        h1=0
        h2=0

        if not root:
            return 

        h1=self.height(root,x)
        h2=self.height(root,y)

        x_par=self.parent(root,x)
        y_par=self.parent(root,y)

        if h1==h2 and x_par!=y_par:
            return True

        return False

    def height(self,root,a):

        if not root:
            return -1
        dist=-1

        if root.val ==a:
            return dist+1
        
        dist=self.height(root.left,a)

        if dist>=0:
            return dist+1
        
        dist=self.height(root.right,a)

        if dist>=0:
            return dist+1
        
        return dist

    def parent(self,node,a):

        if not node:
            return
        
        if (node.left and node.left.val==a) or (node.right and node.right.val==a):
            return node.val
        #search in the left tree
        left_parent=self.parent(node.left,a)

        if left_parent:
            return left_parent
        #search in the right tree
        right_parent=self.parent(node.right,a)

        if right_parent:
            return right_parent


