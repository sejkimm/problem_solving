from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseAndInvert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = self.traverseAndInvert(
            root.right
        ), self.traverseAndInvert(root.left)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.traverseAndInvert(root)
