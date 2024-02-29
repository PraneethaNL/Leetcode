#QUESTION:
# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

#ALGO:

#Level order traversal/ BFS with some 'if' statements.

#TC - O(n) - same as bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q=deque([root])
        level=0
        while q:
            n= len(q)
            if level%2==0:
                prev=float('-inf')
            else:
                prev=float('inf')
            for i in range(n):
                node=q.popleft()
                curr=node.val
                #even level - odd ints,increasing
                if level&1==0:
                    if curr&1==0:
                        return False
                    else:
                        if curr<=prev:
                            return False
                        prev=curr
                #odd level- even ints,decreasing
                else:
                    if curr&1==1:
                        return False
                    else:
                        if curr>=prev:
                            return False
                        prev=curr
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return True




    