from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


# ---- simple test cases ----
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Input: [0,1,2,3]
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
out = Solution().reverseList(head)
print(to_list(out))  # [3,2,1,0]

# Input: [1,2]
head = ListNode(1, ListNode(2))
print(to_list(Solution().reverseList(head)))  # [2,1]

# Input: [1]
head = ListNode(1)
print(to_list(Solution().reverseList(head)))  # [1]

# Input: []
print(to_list(Solution().reverseList(None)))  # []
