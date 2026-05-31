"""
Count Good Nodes in Binary Tree
Medium
Topics
Company Tags
Hints
Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:



Input: root = [2,1,1,3,null,1,5]

Output: 3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_value):
            if not root:
                return 0

            count = 1 if root.val >= max_value else 0 # current node
            max_value = max(root.val, max_value)
            count += dfs(root.left, max_value) + dfs(root.right, max_value)

            return count
        
        return dfs(root, root.val)