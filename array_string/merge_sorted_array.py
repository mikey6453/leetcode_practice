from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1 # pointer for greatest value of nums1, nums2, and the end of nums1

        while j >= 0: # loop until finish nums2
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


# Test cases
sol = Solution()

# 1. Normal merge
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
sol.merge(nums1, 3, nums2, 3)
print(nums1)  # Expected: [1,2,2,3,5,6]

# 2. nums1 has all smaller numbers
nums1 = [1,2,4,0,0,0]
nums2 = [5,6,7]
sol.merge(nums1, 3, nums2, 3)
print(nums1)  # Expected: [1,2,4,5,6,7]

# 3. nums1 has all larger numbers
nums1 = [7,8,9,0,0,0]
nums2 = [1,2,3]
sol.merge(nums1, 3, nums2, 3)
print(nums1)  # Expected: [1,2,3,7,8,9]
