from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    inOrderTreeNodeVal: List[int] = []

    def traverseInOrder(self, treeNode: Optional[TreeNode]) -> None:
        if treeNode is None:
            return None

        self.traverseInOrder(treeNode.left)
        self.inOrderTreeNodeVal.append(treeNode.val)
        self.traverseInOrder(treeNode.right)

        return None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inOrderTreeNodeVal = []
        self.traverseInOrder(root)

        minDiff = 2**63 - 1

        for early, late in zip(self.inOrderTreeNodeVal, self.inOrderTreeNodeVal[1:]):
            minDiff = min(minDiff, (late - early))

        return minDiff
