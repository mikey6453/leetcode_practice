# 122. Best Time to Buy and Sell Stock II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, L = 0, 0

        for R in range(len(prices)):
            if prices[R] > prices[L]:
                max_profit += prices[R] - prices[L]
            L = R
        

        return max_profit
    

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,3,4,5]))
print(solution.maxProfit([7,6,4,3,1]))


"""
Use the sliding window technique. Greed condition: anytime you can make a profit, immediately buy and sell for those days. and add to the max profit.
Move pointer when making a profit or when you find a lower price than the current day.
"""
