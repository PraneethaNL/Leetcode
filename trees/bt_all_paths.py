#QUESTION:
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def dfs(root,s):
            s+=str(root.val)
            if not root.left and not root.right:
                res.append(s)
                return
            if root.right:
                dfs(root.right,s+"->")
            if root.left:
                dfs(root.left,s+"->")
        
        dfs(root,"")
        return res


# OR
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# import copy
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         paths=[]
#         curr_path=[]

#         def dfs(root)->None:
#             if not root:
#                 return
#             curr_path.append(str(root.val))
    
    #deepcopy is imp, otherwise for some reason the curr_path 
    #is not getting copied properly/
    #if I append curr_path directly to paths it outputs empty lists
    
#             if not root.left and not root.right:
    
#                 ls=copy.deepcopy(curr_path)
#                 #print(curr_path)
#                 s="->".join(ls)
#                 paths.append(s)
    
#             dfs(root.left)
#             dfs(root.right)
#             curr_path.pop()

#         dfs(root)

#         #print(paths)

#         return paths

    
        
