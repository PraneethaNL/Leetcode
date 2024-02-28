#QUESTION:
#Given the root of a binary tree, return the leftmost value in the LAST ROW of the tree.

#ALGO:

#But I feel there is a catch to this, there can be a case where the last row might not contain any node that is the left child of it's parent.

#since the question explicitly says leftchild in last row only- so there are no cases like above, otherwise they would have mentioned
#if there is no such node, return none or something.

# Find depth of the tree and do bfs to reach the last level/row and 
# then return the first element's value from the que.

#OR

#Do normal levelorder traversal and return the first element of the last level.
#using deque() instead of a normal list - runs faster.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q=deque([root])
        res=root.val
        while q:
            first=False
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if not first:
                    first=True
                    res=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
        

        # q=[]
        # q.append(root)
        # #depth = self.depth(root)
        # res=[]
        # while q:
        #     n=len(q)
        #     level=[]
        #     # if depth==1:
        #     #     break
        #     for i in range(n):
        #         node=q.pop(0)
        #         level.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     if level:
        #         res.append(level)
        #     #depth-=1
        # return res[-1][0]   

    # def depth(self,root):
    #     left=0
    #     right=0

    #     if root:
    #         left=1+self.depth(root.left)
    #         right=1+self.depth(root.right)
    #     return max(left,right)
        