#QUESTION: Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res =0
        l=0
        r=0

        if root:
            #if root.left:
            l = 1+self.maxDepth(root.left)
            # if root.right:
            r = 1+self.maxDepth(root.right)
            
            
        res = max(l,r)
        return res