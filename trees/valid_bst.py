"""
Valid Binary Search Tree
Medium
Topics
Company Tags
Hints
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:



Input: root = [2,1,3]

Output: true
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root: Optional[TreeNode], left, right):
            if not root:
                return True

            if not (root.val > left and root.val < right):
                return False

            return valid(root.left, left, root.val) and valid(root.right, root.val, right)

        return valid(root, float('-inf'), float('inf'))
    

"""
1. The root can be any value, however all the values in the right have to be strictly greater than the root
2. and all the values in the left have to be strictly greater than the root
3. Use recursion to figuer out if the subtrees are within the correct bounds. if they are not return false.
4. Return true if both the left and right subtrees have valid values.
"""