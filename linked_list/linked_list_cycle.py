from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"ListNode({self.val})"


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False


# ---------- Helper function to create cycles ----------

def create_linked_list(values, pos):
    """
    values: list of node values
    pos: index where tail connects (-1 means no cycle)
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# ---------- Test cases ----------

solution = Solution()

# Test 1: cycle exists (tail connects to index 1)
head = create_linked_list([3, 2, 0, -4], 1)
print("Test 1 (cycle):", solution.hasCycle(head))  # True

# Test 2: no cycle
head = create_linked_list([1, 2, 3, 4], -1)
print("Test 2 (no cycle):", solution.hasCycle(head))  # False

# Test 3: single node with cycle
head = create_linked_list([1], 0)
print("Test 3 (single node cycle):", solution.hasCycle(head))  # True

# Test 4: single node no cycle
head = create_linked_list([1], -1)
print("Test 4 (single node no cycle):", solution.hasCycle(head))  # False

# Test 5: empty list
head = create_linked_list([], -1)
print("Test 5 (empty list):", solution.hasCycle(head))  # False
