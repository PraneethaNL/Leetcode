#question : Binary Tree Zigzag Level Order Traversal
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

#Algo:
#this is the regular level order/bfs
#use deque so that we can pop from start of the queue
#traverse the que while appending each of its node value to the level list
# and also append the node children to the que from right, basically append is fine.
#use the 'direction' flag to toggle from left->right to right->left, start the algo with left->right
#if right-> left then we'll reverse the level list and then append it to final result.



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
                        
                    
        
