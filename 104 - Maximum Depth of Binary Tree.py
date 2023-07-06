"""
Leetcode 104 - Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

Solution is derived using recursion to recursively call height function until all leaf nodes are found
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            elif root.left is None and root.right is None:
                return 1
            return max(height(root.left), height(root.right))+1
        return height(root)
