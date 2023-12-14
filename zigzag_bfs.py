#question
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        que=deque()
        
        res=[]
        
        
        que.append(root)
        direction =0 #start with left to right at root
        
        while que:
            n=len(que)
            level=[]
            
            for i in range(n):
                node=que.popleft()
                if node:
                    level.append(node.val)
                    
                    que.append(node.left)
                    que.append(node.right)
                    
            if level:
                if direction:
                    level.reverse()
                res.append(level)
                
            if direction:
                direction=0
            else:
                direction =1
        return res
                        
                    
        