#QUESTION: Lowest Common Ancestor of a Binary Search Tree

#ALGO:

#Check how the values of the nodes compare to the root.
#If they are both greater than the root, then we need to check the right tree
#If they are both less than the root, then we need to check the left tree.
#If not, i.e. one is less than the root and the other is greater than the root, then root itself is
#their common ancestor.

#OR

# This will work for both BST and binary Tree:
    
# Similar to cousins in a tree problem.
# Find the depth of the nodes and ancestors - use the find parent code here
# Store the ancestors in a dict, and traverse one of these and check if we can find any of its values in the other dictionary.
#if so, return the first such encounter.( since the dictionary stores ancestors maintaining the order).

# The above solution is space efficient, can do better for time complexity.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        curr=root
        while curr:
            if p.val>curr.val and q.val > curr.val:
                curr=curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr=curr.left
            else:
                return curr
            
    #OR 
    #This works for both bst and binary tree
    #     p1={}
    #     p2={}

    #     p1[p]=p.val
    #     p2[q]=q.val

    #     p1_d=self.depth(root,p)
    #     p2_d=self.depth(root,q)

    #     temp1=p
        
    #     while p1_d and temp1:
    #         temp1=self.parent(root,temp1)
    #         if temp1:
    #             p1[temp1]=temp1.val
                
    #         p1_d-=1
    #     print(p1.values())

    #     temp2=q
        
    #     while p2_d and temp2:
    #         temp2=self.parent(root,temp2)
    #         if temp2:
    #             p2[temp2]=temp2.val    
    #         p2_d-=1
        
    #     for i in p1:
    #         if i in p2:
    #             return i
    #     return None

    # def depth(self,root,node):

    #     if not root:
    #         return -1

    #     dist=-1

    #     if root==node:
    #         return dist+1
        
    #     dist=self.depth(root.left,node)

    #     if dist>=0:
    #         return dist+1

    #     dist=self.depth(root.right,node)

    #     if dist>=0:
    #         return dist+1

    #     return dist

    
    # def parent(self,root,node):
    #     if not root:
    #         return None
        
    #     if (root.left and root.left.val==node.val) or (root.right and root.right.val == node.val):
    #         return root
        
    #     left_parent=self.parent(root.left,node)

    #     if left_parent:
    #         return left_parent
        
    #     right_parent=self.parent(root.right,node)

    #     if right_parent:
    #         return right_parent

       
        
        
        