"""
Subsets II
Medium
Topics
Company Tags
Hints
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
Constraints:

1 <= nums.length <= 11
-20 <= nums[i] <= 20
"""


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curSet, subSet = [], []
        self.traverse(0, curSet, subSet, nums)
        return subSet
    
    def traverse(self, i, curSet, subSet, nums):
        if i >= len(nums):
            subSet.append(curSet.copy())
            return
        
        # include ith value
        curSet.append(nums[i])
        self.traverse(i + 1, curSet, subSet, nums)

        # do not include ith value
        curSet.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.traverse(i + 1, curSet, subSet, nums)