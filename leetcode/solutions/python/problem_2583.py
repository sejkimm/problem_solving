from typing import Dict, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    treeNodeByLevel: Dict[int, List[int]] = {}

    def traverseTree(self, currentNode: Optional[TreeNode], currentLevel: int) -> None:
        if currentNode is None:
            return None

        if currentLevel not in self.treeNodeByLevel:
            self.treeNodeByLevel[currentLevel] = [currentNode.val]
        else:
            self.treeNodeByLevel[currentLevel].append(currentNode.val)

        self.traverseTree(currentNode.left, currentLevel + 1)
        self.traverseTree(currentNode.right, currentLevel + 1)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.treeNodeByLevel = {}

        self.traverseTree(root, 1)

        return (
            sum(sorted(self.treeNodeByLevel.items(), key=lambda item: sum(item[1]), reverse=True)[k - 1][1])
            if len(self.treeNodeByLevel.keys()) >= k
            else -1
        )
