# Sliding Window Maximum
# Solved 
# Hard
# Company Tags
# Hints
# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6
# Constraints:

# 1 <= nums.length <= 1000
# -10,000 <= nums[i] <= 10,000
# 1 <= k <= nums.length


from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()

        for i in range(len(nums)):
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            
            if i + 1  >= k:
                result.append(nums[queue[0]])
        

        return result
    

Test1 = Solution()
Test2 = Solution()


print(Test1.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Test2.maxSlidingWindow([1], 1))