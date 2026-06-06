"""
Merge K Sorted Linked Lists
Hard
Topics
Company Tags
Hints
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
Constraints:

0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000
"""



# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            
            lists = mergedLists
        
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dummy.next


"""
Use a divde and conquer strategy where you combine every two lists and repeat until there is one linked list in the array. if there is an odd number of linked lists merge 
the last linked list with an empty linked lists (none). Use a helper function merge two sorted linked lists.
"""