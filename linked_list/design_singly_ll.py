"""
Design Singly Linked List
Easy
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
Example 1:

Input: 
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
Note:

The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.
"""

class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node


class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, i: int) -> int:
        curr = self.head.next
        index = 0
        while curr:
            if index == i:
                return curr.val
            index += 1
            curr = curr.next
        
        return -1
            
    
    def insertHead(self, val: int):
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int):
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    
    def remove(self, i: int) -> bool:
        index = 0
        prev = self.head

        while prev.next:
            if index == i:
                if prev.next == self.tail:
                    self.tail = prev
                prev.next = prev.next.next
                return True
            prev = prev.next
            index += 1
        
        return False
    

    def getValues(self):
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next
        
        return result
    

# 1. Create a helper listnode class and initialize with head and tail pointers with a dummy node
