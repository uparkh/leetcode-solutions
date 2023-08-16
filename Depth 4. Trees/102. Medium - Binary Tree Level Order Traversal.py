# TOTAL TIME TAKEN: 14m, 28s 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque

# My Original Solution, O(n) time, O(n) memory
# This BFS level traversal and encoding into an array can be done
# on any generic tree, not just a BST. This does not use any property
# of a BST to generate the final answer. 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        q = deque()
        if root: q.append(root)
        while q:
            res.append([])
            for i in range(len(q)):
                curr = q.popleft()
                res[-1].append(curr.val)
                if curr.left:  q.append(curr.left)
                if curr.right: q.append(curr.right)
        return res
    
# NeetCode Solution - O(n) time, O(n) memory

# Pretty much my exact solution. This solution also not exclusive to BSTs.
# I think mine is just a tad bit more efficient memory-wise and slightly worse
# runtime-wise because I do not create a |val| nested array to be processed
# before appending it to the |res| outer array, and take a small bit of runtime
# to instead access the available information using [-1] accesses. Minor
# differences, however. 

# Nevermind, just tested it, and it is around 8% worse runtime and A LOT worse
# memory-wise. Seems that not only does his solution reserve extra space:
# once for |val| and another for appending it to |res|, but also more time to
# actually append |val| to |res|. Maybe because the algorithm is so simple 
# and straightforward, that when standardized, the differences are exaggerated,
# when in reality the actual memory/runtime difference is 0.1 MB/2ms 
import collections
from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res