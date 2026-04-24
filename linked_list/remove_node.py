"""
Remove Node From End of Linked List
Medium
Topics
Company Tags
Hints
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"
    

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        L = dummy
        R = head

        while n > 0 and R:
            R = R.next
            n -= 1
        
        while R:
            L = L.next
            R = R.next
        
        L.next = L.next.next

        return dummy.next

        
        

# 1. Use left and right pointers to find the nth node from the list
# 2. Use dummy node to point to the node right before the nth node
# 3. point that node to the node afterwards