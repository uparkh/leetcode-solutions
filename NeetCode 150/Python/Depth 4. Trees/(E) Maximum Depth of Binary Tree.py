# TOTAL TIME TAKEN: <10 minutes
# My Original Solution - O(n) time, O(log n) memory
# The only way I can think of to do this with recursion is with a global
# or static variable.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node_stack, depth_stack = [], []
        res = 0
        if root:
            node_stack.append(root)
            depth_stack.append(1)
        while node_stack:
            curr_node = node_stack.pop()
            curr_depth = depth_stack.pop()
            res = max(res, curr_depth)
            if curr_node.left:
                node_stack.append(curr_node.left)
                depth_stack.append(curr_depth + 1)
            if curr_node.right:
                node_stack.append(curr_node.right)
                depth_stack.append(curr_depth + 1)
        return res

# NeetCode has 3 different solutions, all 3 are valuable enough to include
# here. He has a simpler Pythonic way of storing the depth and node stack
# information, so his iterative DFS solution looks much cleaner than mine.
# I did not think of that way of doing the recursive solution, but it does make
# perfect sense. The base case of null ptr is caught, and the max function
# correctly returns the maximum depth.

# RECURSIVE DFS
class NeetCodeSolution1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ITERATIVE DFS
class NeetCodeSolution2:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

from collections import deque
# BFS
class NeetCodeSolution3:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
