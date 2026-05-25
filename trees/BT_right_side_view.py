"""
Binary Tree Right Side View
Medium
Topics
Company Tags
Hints
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:



Input: root = [1,2,3,null,4,null,5]

Output: [1,3,5]
Example 2:



Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]
Example 3:

Input: root = [1,null,2]

Output: [1,2]
Example 4:

Input: root = []

Output: []
"""

from ast import List
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                if len(level) == 0:
                    result.append(curr.val)
                level.append(curr.val)
        
        return result
            