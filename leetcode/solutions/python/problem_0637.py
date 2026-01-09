from typing import Dict, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    treeDictByDepth: Dict[int, List[int]] = {}

    def createTreeDictByDepth(
        self, treeNode: Optional[TreeNode], currentDepth: int
    ) -> None:
        if treeNode is None:
            return None

        if currentDepth in self.treeDictByDepth:
            self.treeDictByDepth[currentDepth].append(treeNode.val)
        else:
            self.treeDictByDepth[currentDepth] = [treeNode.val]

        self.createTreeDictByDepth(treeNode.left, currentDepth + 1)
        self.createTreeDictByDepth(treeNode.right, currentDepth + 1)

        return None

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.treeDictByDepth = {}
        self.createTreeDictByDepth(root, 0)

        avgNodeVal: List[float] = []

        for _, nodeVals in sorted(self.treeDictByDepth.items(), key=lambda x: x[0]):
            avgNodeVal.append(sum(nodeVals) / len(nodeVals))

        return avgNodeVal
