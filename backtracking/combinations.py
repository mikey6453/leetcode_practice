"""
Combinations
Medium
Topics
Company Tags
You are given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 3, k = 2

Output: [
    [1,2],
    [1,3],
    [2,3]
]
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.backtrack(1, n, k, [], combs)
        return combs

    def backtrack(self, i, n, k, curComb, combs):
        if len(curComb) == k:
            combs.append(curComb.copy())
            return
        
        if i > n:
            return
        
        for j in range(i, n+1):
            curComb.append(j)
            self.backtrack(j + 1, n, k, curComb, combs)
            curComb.pop()



"""
The idea is to make a decision tree of height k, where you try out all the combinations. Inorder to avoid duplicates,
after choosing a value and getting its combinations, you can't use that same value when creating combinations with other values
"""