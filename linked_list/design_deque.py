"""
Design Double-ended Queue
Easy
Design a Double-ended Queue class.

Your Deque class should support the following operations:

Deque() will initialize an empty queue.
bool isEmpty() will return whether the queue is empty or not.
void append(int value) will insert value at the end of the queue.
void appendleft(int val) will insert value at the beginning of the queue.
int pop() will remove and return the value at the end of the queue. If the queue is empty, return -1.
int popleft() will remove and return the value at the beginning of the queue. If the queue is empty, return -1.
Note: You should implement each operation in 
O
(
1
)
O(1) time complexity.

Example 1:

Input:
["isEmpty", "append", 10, "isEmpty", "appendLeft", 20, "popLeft", "pop", "pop", "append", 30, "pop", "isEmpty"]

Output:
[true, null, false, null, 20, 10, -1, null, 30, true]
"""

class ListNode:

    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


class Deque:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def isEmpty(self) -> bool:
        return False if self.head.next else True


    def append(self, value: int):
        new_node = ListNode(value)
        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = self.tail.next
        

    def appendleft(self, val: int):
        new_node = ListNode(val)
        second = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = second

        if second:
            second.prev = new_node
        else:
            self.tail = new_node

    
    def pop(self) -> int:
        if not self.head.next:
            return -1

        result = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        return result.val


    def popleft(self) -> int:
        if not self.head.next:
            return -1
        
        result = self.head.next
        first = self.head.next.next

        self.head.next = first

        if first:
            first.prev = self.head
        else:
            self.tail = self.head
        
        return result.val


# 1. Utilize a doubly linked list for the double ended queue remember edge cases of list size of 0 and 1