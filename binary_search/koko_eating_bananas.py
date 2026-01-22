import math
from typing import List


# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = max(piles)
        L, R = 1, max(piles)

        while L <= R:
            mid = (L+R) // 2
            if self.isvalidanswer(mid, piles, h):
                result = min(result, mid)
                R = mid - 1
            else:
                L = mid + 1
        
        return result
    

    def isvalidanswer(self, hours, piles, h):
        time = 0
        for i in range(len(piles)):
            time += math.ceil(piles[i]/hours)
        
        return time <= h


test = Solution()
print(test.minEatingSpeed([3,6,7,11], 8))
print(test.minEatingSpeed([30,11,23,4,20], 5))
print(test.minEatingSpeed([30,11,23,4,20], 6))

"""
slowest speed is 1 and fastest is the greatest piles amount. Use binary search to find the slowest speed faster than h.
"""