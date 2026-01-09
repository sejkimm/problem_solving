from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchWithSum(
        self, treeNode: Optional[TreeNode], currentSum: int, targetSum: int
    ) -> bool:
        if treeNode.left is None and treeNode.right is None:
            return (currentSum + treeNode.val) == targetSum

        leftPathAvailability: bool = False
        rightPathAvailability: bool = False

        if treeNode.left is not None:
            leftPathAvailability = self.searchWithSum(
                treeNode.left, currentSum + treeNode.val, targetSum
            )
        if treeNode.right is not None:
            rightPathAvailability = self.searchWithSum(
                treeNode.right, currentSum + treeNode.val, targetSum
            )

        return leftPathAvailability or rightPathAvailability

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        return self.searchWithSum(root, 0, targetSum)
