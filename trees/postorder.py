#Question: Post-order traversal of a binary tree

#Algo:

# left, right, root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root:
            out.extend(self.postorderTraversal(root.left))
            out.extend(self.postorderTraversal(root.right))
            out.append(root.val)
        
        return out
        