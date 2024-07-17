# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,arr):
            if node is None:
                return 
            if node.left is None and node.right is None:
                arr.append(node.val)
            else:
                dfs(node.left,arr)
                dfs(node.right,arr)
        ar1 = []
        ar2 = []
        dfs(root1,ar1)
        dfs(root2,ar2)
        return ar1 ==ar2