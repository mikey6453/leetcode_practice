"""
Invert Binary Tree
Easy
Topics
Company Tags
Hints
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]

"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_binary_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.left, self.right = self.right, self.left


        self.invert_binary_tree(root.right)
        self.invert_binary_tree(root.left)

        return root

