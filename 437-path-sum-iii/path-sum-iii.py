# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        if root == None:
            return 0
        l = []
        def gen(curr,s,v):
            if curr==None:
                return
            if s==target:
                l.append(1)
            if curr.left:
                gen(curr.left,s+curr.left.val,v+[curr.left.val])
            if curr.right:
                gen(curr.right,s+curr.right.val,v+[curr.right.val])
        def inorder(root):
            if root:
                gen(root,root.val,[root.val])
                inorder(root.left)
                inorder(root.right)
        inorder(root)
        return sum(l)