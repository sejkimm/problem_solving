from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def breadthFirstTraverse(
        self, currentNode: Optional[TreeNode], leftFirst: bool
    ) -> List[Optional[int]]:

        bfs_queue: List[int] = []
        traverse: List[Optional[int]] = []

        bfs_queue.append(currentNode)

        while len(bfs_queue) != 0:
            currentNode = bfs_queue.pop(0)

            if currentNode is None:
                traverse.append(None)
                continue
            else:
                traverse.append(currentNode.val)

            if leftFirst:
                bfs_queue.append(currentNode.left)
                bfs_queue.append(currentNode.right)
            else:
                bfs_queue.append(currentNode.right)
                bfs_queue.append(currentNode.left)

        return traverse

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftTreeTraverse: List[Optional[int]] = self.breadthFirstTraverse(
            root.left, leftFirst=True
        )
        rightTreeTraverse: List[Optional[int]] = self.breadthFirstTraverse(
            root.right, leftFirst=False
        )

        return leftTreeTraverse == rightTreeTraverse
