# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        max_so_far = -float("inf")
        count = 0

        def dfs(node):
            nonlocal max_so_far, count
            max_so_far_tmp = max_so_far

            if node is None:
                return
            
            if node.val >= max_so_far:
                count += 1
                max_so_far = node.val

            dfs(node.left)
            dfs(node.right)
            max_so_far = max_so_far_tmp

        dfs(root)

        return count


        