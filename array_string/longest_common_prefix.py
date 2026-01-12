# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start by assuming the entire first string is the prefix.
        prefix = strs[0]

        # Compare the current prefix with each other string.
        for s in strs[1:]:
            # Find how many characters match from the start.
            i = 0
            limit = min(len(prefix), len(s))
            while i < limit and prefix[i] == s[i]:
                i += 1

            # Shrink prefix to only the matching part.
            prefix = prefix[:i]

            # If nothing matches, we're done early.
            if prefix == "":
                return ""

        return prefix


# Quick checks
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     # ""