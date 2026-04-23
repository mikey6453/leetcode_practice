# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linked_list.linked_list_cycle import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        # merge alternating
        second = prev

        while second:
            temp1 = head.next
            temp2 = second.next

            head.next = second
            second.next = temp1
            
            head = temp1
            second = temp2