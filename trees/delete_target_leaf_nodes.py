"""
Delete Leaves With a Given Value
Medium
Topics
Company Tags
You are given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

Example 1:

Input: root = [1,2,3,5,2,2,5], target = 2

Output: [1,2,3,5,null,null,5]
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # leaf node
        if root.left == None and root.right == None and root.val == target:
            return None

        return root


"""
use postorder traversal so you can process the children and remove before checking to see if you need to 
remove the parent nodes if they become removalbe child nodes as well
"""