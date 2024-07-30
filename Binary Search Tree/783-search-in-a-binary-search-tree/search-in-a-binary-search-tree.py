class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.right and root.val<val: root=root.right
            elif root.left and root.val>val: root=root.left
            elif root.val==val: return root
            else: break
        return None