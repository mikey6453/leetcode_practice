from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next


# ---------- Helper functions ----------

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------- Test cases ----------

solution = Solution()

# Test 1: normal case
l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])
merged = solution.mergeTwoLists(l1, l2)
print("Test 1:", linked_list_to_list(merged))  # [1, 1, 2, 3, 4, 4]

# Test 2: one empty list
l1 = build_linked_list([])
l2 = build_linked_list([0])
merged = solution.mergeTwoLists(l1, l2)
print("Test 2:", linked_list_to_list(merged))  # [0]

# Test 3: both empty
l1 = build_linked_list([])
l2 = build_linked_list([])
merged = solution.mergeTwoLists(l1, l2)
print("Test 3:", linked_list_to_list(merged))  # []

# Test 4: unequal lengths
l1 = build_linked_list([1, 3, 5, 7])
l2 = build_linked_list([2, 4])
merged = solution.mergeTwoLists(l1, l2)
print("Test 4:", linked_list_to_list(merged))  # [1,2,3,4,5,7]


