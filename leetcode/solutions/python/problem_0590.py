from typing import List


class Solution:

    route: List[int] = []

    def traverse(self, node: "Node") -> None:

        if node.children is not None:
            for child_node in node.children:
                self.traverse(child_node)

        self.route.append(node.val)

    def postorder(self, root: "Node") -> List[int]:
        self.route = []

        if root is not None:
            self.traverse(root)

        return self.route
