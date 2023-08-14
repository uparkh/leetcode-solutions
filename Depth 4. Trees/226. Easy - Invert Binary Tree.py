# TOTAL TIME: 16m, 14s

# My Original Solution - O(n) runtime, O(1) space
# Using iterative pre-order traversal/DFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        if root: stack.append(root)
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
            tmp = curr.right
            curr.right = curr.left
            curr.left = tmp
        return root

# NeetCode Solution - O(n) runtime, O(1) space
# Using recursive pre-order traversal.
# Apparently recursion is faster here than the iterative version?
# I get the memory usage for a recursive solution is better, due to not having to store
# a stack, but it doesn't make sense that it's faster.
# Actually, it may be faster here because it is tail-end recursion, and perhaps the
# Python interpreter is optimizing that at a core level.
class NeetCodeSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
