"""
Binary Tree Level Order Traversal
Medium
Topics
Company Tags
Hints
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right


class Solution:
    def binary_level_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                level.append(curr.val)
            
            result.append(level)

        return result