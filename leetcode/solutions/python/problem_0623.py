from collections import deque
from typing import Optional, List
from common.tree_node import TreeNode, parse_treenode_to_list


class Solution:
    depth: int = -1
    val: int = -1
    root: Optional[TreeNode] = None

    def traverse_and_insert(
        self, parent_node: Optional[TreeNode], current_node: Optional[TreeNode], current_depth: int, is_left_node: bool
    ) -> None:
        if self.depth == 1 and current_depth == 1:
            new_root = TreeNode(self.val, current_node, None)
            self.root = new_root

        elif current_depth == self.depth:
            new_node = TreeNode()
            new_node.val = self.val
                
            if is_left_node:
                parent_node.left = new_node
                new_node.left = current_node
                new_node.right = None
            else:
                parent_node.right = new_node
                new_node.left = None
                new_node.right = current_node

        if current_node is None:
            return None

        self.traverse_and_insert(current_node, current_node.left, current_depth + 1, True)
        self.traverse_and_insert(current_node, current_node.right, current_depth + 1, False)

        return None

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.depth = depth
        self.val = val
        self.root = root

        self.traverse_and_insert(parent_node=None, current_node=root, current_depth=1, is_left_node=True)

        return self.root
