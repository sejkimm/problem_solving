from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchMaxDepth(self, treeNode: Optional[TreeNode], depth: int) -> int:
        if treeNode is None:
            return depth

        return max(self.searchMaxDepth(treeNode.left, depth + 1), self.searchMaxDepth(treeNode.right, depth + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.searchMaxDepth(root, 0)
