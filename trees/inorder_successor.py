#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        
        inord=self.inorder(root)
        print(inord)
        
        for i in range(len(inord)):
            if i==len(inord)-1:
                return None
            if inord[i]==x:
                return inord[i+1]
    
    def inorder(self,root):
        res=[]
        
        if root:
            res.extend(self.inorder(root.left))
            res.append(root)
            res.extend(self.inorder(root.right))
        
        return res