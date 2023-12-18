#question
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/

#Algo:

# first element in preorder traversal is the root of the tree.
# Traverse the preorder list, find the index of the corresponding element within inorder list as "ind"
# all the elements before this index in inorder list will fall in the left subtree (apply builtree here,#recursion) and
# all the elements after the index will come under the right subtree (call builtree here again #recursion).
# make sure to put the bound check for 'ind'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        val=preorder[0]
        
        root=TreeNode(val)
            
        ind=inorder.index(val)
        
        del preorder[0]
        
        if ind >0 or ind < len(inorder)-1:

            root.left=self.buildTree(preorder,inorder[:ind])
            root.right=self.buildTree(preorder,inorder[ind+1:])
        
        return root
        
        


        