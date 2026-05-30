"""
Balanced Binary Tree
Easy
Topics
Company Tags
Hints
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: true
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: List[TreeNode]):
        return self.dfs(root)[0]


    def dfs(self, root: List[TreeNode]):
        if not root:
            return [True, 0]
        
        left = self.dfs(root.left)
        right = self.dfs(root.right) 

        balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
        return [balanced, max(left[1], right[1]) + 1]
