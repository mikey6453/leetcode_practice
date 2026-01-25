# 704. Binary Search
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L + R) // 2
            if target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else:
                return mid
        
        return -1
    

Test1 = Solution()
Test2 = Solution()
print(Test1.search([-1,0,3,5,9,12], 9))
print(Test2.search([-1,0,3,5,9,12], 2))


"""
Use Binary search, O(log(n)). While the L is to the left or at the R pointer, find the mid point and eliminate half the space by comparing if it is greater than or less than the target. If it is the target, then return
that value.
"""