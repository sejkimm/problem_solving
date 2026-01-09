from typing import Optional, Set


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen: Set[ListNode] = set()
        current_node: ListNode = head

        if head is None:
            return False

        while current_node.next is not None:
            if current_node in seen:
                return True

            seen.add(current_node)
            current_node = current_node.next

        return False
