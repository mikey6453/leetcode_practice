"""
Letter Combinations of a Phone Number
Medium
Topics
Company Tags
Hints
You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.

Phone keypad letter mapping

Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.backtrack(digits, phone, result, "", 0)
        return result


    def backtrack(self, digits, phone, result, curComb, i):
        if len(curComb) == len(digits):
            result.append(curComb)
            return

        if i > len(digits):
            return
        
        for letter in phone[digits[i]]:
            self.backtrack(digits, phone, result, curComb + letter, i + 1)


"""
use a phonebook to map each number to their respective letters. Use a for loop and recursion to simulate a double for loop in a way.
append when you reach correct length, when you backtrack a letter, increment i to create the combinations with the current letter 
and every letter of the incremented ith value.
"""