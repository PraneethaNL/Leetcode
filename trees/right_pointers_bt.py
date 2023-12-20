
#Question:  Populating Next Right Pointers in Each Node

#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/


#Algo:
# Use bfs, intialize a list q that has the left and right children of the root along with None
# traverse q by popping an element from start, 
# point the 'next' for popped node to the starting node in q.
# if we encounter 'None', it means end of that level so check if the q is empty, if not then append None in the end and skip the next steps in the iteration.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return 
        
        #tree has only one node, i.e root
        if not root.right:
            root.next=None
            return root
        
        q=[root.left,root.right,None]
        
        root.next=None
        
        while q:
            node=q.pop(0)
            #end of a level
            if not node:
                #if it's the last level, i.e all leaf nodes are done and q is empty
                if not q:
                    return root
                q.append(None)
                continue
            node.next=q[0]
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            
        return root
            
        
        
        
                
                
                
                
            
        
        