"""
Path Sum
Easy
Topics
Company Tags
You are given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:



Input: root = [1,2,3], targetSum = 3

Output: true
Explanation: The root-to-leaf path with the target sum is 1 -> 2.
"""


from typing import Optional

from trees.bst_insert import TreeNode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, currSum):
            if not root:
                return False

            currSum += root.val

            if not root.left and not root.right and currSum == targetSum:
                return True

            if dfs(root.left, currSum): return True
            if dfs(root.right, currSum): return True

            currSum -= root.val

            return False
            
        return dfs(root, 0)