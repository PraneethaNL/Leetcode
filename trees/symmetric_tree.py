#QUESTION:

#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

#Eg;
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror(left,right):
            if left == None or right == None:
                return left==right
            return (left.val == right.val) and mirror(left.left,right.right) and mirror(left.right,right.left)
        
        return mirror(root.left,root.right)