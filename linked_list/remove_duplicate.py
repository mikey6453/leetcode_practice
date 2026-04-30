"""
83. Remove Duplicates from Sorted List
Solved
Easy
Topics
premium lock icon
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


from typing import Optional

from linked_list.add_two_numbers import ListNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        
        return head
    

def test_delete_duplicates():
    sol = Solution()

    test_cases = [
        # (input, expected_output)
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),  # no duplicates
        ([], []),  # empty list
        ([1], [1]),  # single node
        ([1, 2, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
    ]

    for i, (input_list, expected) in enumerate(test_cases):
        head = build_linked_list(input_list)
        result_head = sol.deleteDuplicates(head)
        result_list = linked_list_to_list(result_head)

        assert result_list == expected, f"Test case {i} failed: expected {expected}, got {result_list}"
        print(f"Test case {i} passed")

if __name__ == "__main__":
    test_delete_duplicates()