"""
Leetcode Problem 111 - Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right:
            return self.minDepth(root.right)+1
        elif root.right is None and root.left:
            return self.minDepth(root.left)+1
        elif root.left is None and root.right is None:
            return 1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1