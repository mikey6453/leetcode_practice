# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                L, R = 0, len(matrix[0])-1
                while L <= R:
                    mid = (L + R) // 2
                    if target < matrix[i][mid]:
                        R = mid - 1
                    elif target > matrix[i][mid]:
                        L = mid + 1
                    else:
                        return True
                
                return False
        
        return False


Test = Solution()
print(Test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


"""
Find the row in which the target is in, return false if not in any rows. Use regular binary search on that row.
"""