#QUESTION:
#Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Input: root = [1,null,2,3]
# Output: [1,2,3]

#ALGO:

#Iterative approach (Faster than recursive approach):

#we should use a stack - because when ever we are replacing recursion call we should use a stack - because function calls are stored in stack.
#we will append our root to the stack
#while stack is not empty - pop the top of the stack and 
#while inserting into the stack - in preorder (root->left->right is the order), we need left val before right
#so, we will push right first and then push left ( since stack is LIFO)

#TC- O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        stack=[]
        stack.append(root)
        while stack:
            top=stack.pop()
            ans.append(top.val)

            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return ans
    

    #Recursive solution:

    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     out =[]
    #     if root:
    #         out.append(root.val)
    #         out.extend(self.preorderTraversal(root.left))
    #         out.extend(self.preorderTraversal(root.right))
    #     return out
        