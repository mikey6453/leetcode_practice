"""
Find the Duplicate Number
Medium
Topics
Company Tags
Hints
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2
Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using 
O
(
1
)
O(1) extra space?

Constraints:

1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                break
        
        return slow


test = Solution()

print(test.findDuplicate([1,2,3,2,2])) # 2
print(test.findDuplicate([1,2,3,4,4])) # 4


# 1. Recognize that this is a linked list cycle: The value of each index points to another index within the array
# 2. Use Floyd's Algorithm: Using fast and slow pointers to iterate across the array (viewed as cycle linked list cycle),
#      - Where they meet is guaranteed to be inside the cycle
#      - the distance from the start to the entrance is equal to that meeting point
#      - this means, if you iterate the current slow pointer and a new slow pointer at the start, they will meet at the start of the linked list