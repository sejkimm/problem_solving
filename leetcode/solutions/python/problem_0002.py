from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        values_int: List[int] = [0, 0]

        for idx, current_listnode in enumerate([l1, l2]):
            multiplier: int = 1

            current_node = current_listnode
            while current_node is not None:
                values_int[idx] += current_node.val * multiplier
                current_node = current_node.next
                multiplier *= 10

        two_value_sum: int = sum(values_int)

        two_value_sum_list: List[int] = []
        while two_value_sum > 0:
            two_value_sum_list.append(two_value_sum % 10)
            two_value_sum //= 10

        two_value_sum_list.reverse()

        listnode_cursor: Optional[ListNode] = None

        for elem in two_value_sum_list:
            first_listnode: ListNode = ListNode(val=elem, next=listnode_cursor)
            listnode_cursor = first_listnode

        if listnode_cursor is None:
            listnode_cursor = ListNode(val=0, next=None)

        return listnode_cursor
