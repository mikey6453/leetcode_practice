
# Code
# Testcase
# Testcase
# Test Result
# 682. Baseball Game
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.


from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []

        for operation in operations:
            if operation == '+':
                ops.append(ops[-1] + ops[-2])
            elif operation == 'D':
                ops.append(ops[-1]*2)
            elif operation == 'C':
                ops.pop()
            else:
                ops.append(int(operation))
            
        return sum(ops)
    
sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))
print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
print(sol.calPoints(["1","C"]))