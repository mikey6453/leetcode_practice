"""
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call pushback(int n) but the array is full, we should resize() the array first.
"""

class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
    

    def get(self, i: int) -> int:
        return self.array[i]

    
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = n
        self.size += 1

    
    def popback(self):
        val = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size -= 1

        return val


    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity

        for i in range(len(self.array)):
            new_array[i] = self.array[i]

        self.array = new_array


    def getSize(self):
        return self.size
    

    def getCapacity(self):
        return self.capacity