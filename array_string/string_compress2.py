"""
Return Compressed String

should return a list of test_input that is compressed or if length is less than 3 just the original letters
"""

test_input = [
    "aaabbbbccd", # a3b4ccdd
    "abcdeeeeee", #
    "aabbccc",
    "aaabbbcccdd",
    "bc" # bc
]

class Solution:
    def compress(self, input: list[str]) -> list[str]:
        result = []

        for curr_str in input:
            compressed = ""
            L = 0

            while L < len(curr_str):
                R = L

                while R < len(curr_str) and curr_str[R] == curr_str[L]:
                    R += 1

                count = R - L

                if count >= 3:
                    compressed += curr_str[L] + str(count)
                else:
                    compressed += curr_str[L] * count

                L = R

            result.append(compressed)

        return result


solution = Solution()
print(solution.compress(test_input))