"""
Combination Sum
Medium
Topics
Company Tags
Hints
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input:
nums = [2,5,6,9]
target = 9

Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.
"""

from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(nums, target, 0, [], result, 0)
        return result

    
    def backtrack(self, nums, target, curSum, curComb, result, start):
        if curSum == target:
            result.append(curComb.copy())
            return
        
        if curSum > target:
            return
        
        for i in range(start, len(nums)):
            curComb.append(nums[i])
            curSum += nums[i]

            self.backtrack(nums, target, curSum, curComb, result, i)

            curComb.pop()
            curSum -= nums[i]
