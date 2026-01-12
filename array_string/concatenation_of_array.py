from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums

        for i in range(len(nums)):
            ans.append(nums[i])

        return ans   
    

sol = Solution()

print(sol.getConcatenation([1,2,1]))
print(sol.getConcatenation([1,3,2,1]))