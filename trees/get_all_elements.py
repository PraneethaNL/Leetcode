#QUESTION: All Elements in Two Binary Search Trees

# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

#ALGO:
# Do inorder traversal of both the trees - this will given us the values of each tree in ascending order.
# Now, apply merge technique from merge sort.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        in1=self.inorder(root1)
        in2=self.inorder(root2)

        i,j=0,0
        l1=len(in1)
        l2=len(in2)
        res=[]

        while i<l1 and j<l2:
            if in1[i]<=in2[j]:
                res.append(in1[i])
                i+=1
            else:
                res.append(in2[j])
                j+=1
        
        while i<l1:
            res.append(in1[i])
            i+=1
        while j<l2:
            res.append(in2[j])
            j+=1
        
        return res

    
    def inorder(self,root):
        res=[]

        if root:
            res.extend(self.inorder(root.left))
            res.append(root.val)
            res.extend(self.inorder(root.right))
        
        return res
        