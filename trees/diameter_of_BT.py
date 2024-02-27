#QUESTION: Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# eg:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


#ALGO:

# sum the left tree height and right tree height at every node and return the maximum of it.

#We cannot just calculate the depth of left subtree and right subtree at root and add them up.
#because there can be a situation where the diameter i.e., max number of edges can be present b/w nodes that are under one subtree.

# eg:
#          4
#     1           2
#             3       4
#           5           6
#             9         7
#expected = 6 (9->5->3->2->4->6->7), but we just add left depth+right depth = 1+4=5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.depth(root)
        
        return self.diameter-2

    def depth(self,root):

        left=0
        right=0

        if root:
            left=1+self.depth(root.left)
            right=1+self.depth(root.right)
        
        if left+right > self.diameter:
            self.diameter=left+right

        return max(left,right)