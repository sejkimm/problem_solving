from typing import Optional
from common.tree_node import TreeNode


class Solution:

    answers = []

    def search(self, current_node: Optional[TreeNode], current_traversal: list) -> None:
        current_traversal.append(str(current_node.val))

        if (current_node.left is None) and (current_node.right is None):
            self.answers.append(current_traversal.copy())

            return None

        if current_node.left is not None:
            self.search(current_node.left, current_traversal)
            current_traversal.pop()

        if current_node.right is not None:
            self.search(current_node.right, current_traversal)
            current_traversal.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.answers = []
        self.search(current_node=root, current_traversal=[])

        return_value = sum((int("".join(answer)) for answer in self.answers))

        return return_value
