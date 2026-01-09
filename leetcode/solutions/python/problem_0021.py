from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list: Optional[ListNode] = ListNode()
        sorted_list_head: Optional[ListNode] = sorted_list

        while list1 is not None or list2 is not None:
            if list1 is None:
                sorted_list.next = ListNode(val=list2.val)
                list2 = list2.next

            elif list2 is None:
                sorted_list.next = ListNode(val=list1.val)
                list1 = list1.next

            else:
                if list1.val < list2.val:
                    sorted_list.next = ListNode(val=list1.val)
                    list1 = list1.next
                else:
                    sorted_list.next = ListNode(val=list2.val)
                    list2 = list2.next

            sorted_list = sorted_list.next

        return sorted_list_head.next
