#QUESTION:
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

#eg:
# Input: root = [1,2,3], targetSum = 5
# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root,0,targetSum)

    def dfs(self,root,sum,target):
        if not root:
            return False
        sum+=root.val
        if not root.left and not root.right:
            return sum==target
        
        return self.dfs(root.left,sum,target) or self.dfs(root.right,sum,target)
        