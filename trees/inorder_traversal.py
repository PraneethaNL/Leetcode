#QUESTION:
#Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]


#ALGO:

#Iterative:

#We can use iteratvie approach for reduced time complexity.
#We will use a stack here
#First we we traverse till the leftmost node while append each node into the stack while traversing.
#now our top of the stack has leftmost node of the tree.
#pop it and apppend it to the ans list.
#if the popped node ( top of the stack) - has right node (this happens when out top is not the leaf ndoe)
#then we will traverse till the left most node in the right subtree while appending each node in the path to the stack.

#TC-O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC- O(n) - since we visit each node once
# Space - O(n) - to store the result.


class Solution:


    #Iterative approach
    #this is comparitively easy to understand
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans=[]
        stack=[]
        curr=root

        while curr:
            stack.append(curr)
            curr=curr.left

        while stack:
            top=stack.pop()
            ans.append(top.val)
            if top.right:
                top=top.right
                while top:
                    stack.append(top)
                    top=top.left
        return ans

    #recurrsion
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res=[]

        #use res+=, instead of extend. This is faster comparitively

        if root:
            res+=self.inorderTraversal(root.left)
            res.append(root.val)
            res+=self.inorderTraversal(root.right)
        
        return res
    
    #Iterative Approach
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
            
        stack = []
        ans = []
        while True:
            while root:
                stack += [root]
                root = root.left
            if not stack:
                return ans
            curr = stack.pop()
            ans += [curr.val]
            root = curr.right
            
        return ans
    
    

        