from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countSubTreeNodes(self, treeNode: Optional[TreeNode]) -> int:
        if treeNode is None:
            return 0

        if treeNode.left is None and treeNode.right is None:
            return 1

        return (
            1
            + self.countSubTreeNodes(treeNode.left)
            + self.countSubTreeNodes(treeNode.right)
        )

    def countNodes(self, root: Optional[TreeNode]) -> int:

        return self.countSubTreeNodes(root)
