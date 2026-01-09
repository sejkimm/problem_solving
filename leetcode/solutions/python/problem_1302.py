from typing import Optional, List, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, node: Optional[TreeNode], depth: int) -> int:
        if node is None:
            return

        if depth in self.treeValByDepth:
            self.treeValByDepth[depth].append(node.val)
        else:
            self.treeValByDepth[depth] = [node.val]
        
        self.traverseTree(node.left, depth+1)
        self.traverseTree(node.right, depth+1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.treeValByDepth: Dict[int, List[int]] = {}
        self.traverseTree(root, 0)

        return sum(self.treeValByDepth[max(self.treeValByDepth.keys())])