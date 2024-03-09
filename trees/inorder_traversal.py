# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC- O(n) - since we visit each node once
# Space - O(n) - to store the result.


class Solution:
    #recurrsion
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res=[]

        #use res+=, instead of extend. This is faster comparitively

        if root:
            res+=self.inorderTraversal(root.left)
            res.append(root.val)
            res+=self.inorderTraversal(root.right)
        
        return res
    
    #iterative
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