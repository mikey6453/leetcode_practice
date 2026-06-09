"""
Binary Tree Maximum Path Sum
Hard
Topics
Company Tags
Hints
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:



Input: root = [1,2,3]

Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0

            # split max
            max_left = dfs(root.left)
            max_right = dfs(root.right)

            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            # compute max path sum with split
            self.res = max(self.res, max_left + max_right + root.val)

            # return max without splitting
            return max(0, max_left, max_right) + root.val

        dfs(root)
        return self.res
