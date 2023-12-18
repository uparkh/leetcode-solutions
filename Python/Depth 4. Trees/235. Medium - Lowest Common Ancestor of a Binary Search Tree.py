# TOTAL TIME: 13m, 35s

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# My Original Solution
# Fundamental intuition: from a top-down BST find, the first node where
# the search direction is split (gotta go left to find one node and right
# to find the other), is the LCA.

# Note that I did not need to check for null left and right pointers
# because in the problem constraints, we are guaranteed that |p| and |q|
# are in the tree. Therefore, if at any conditional we deduce that we need
# to go left or right to find a node, we're also guaranteed that the left
# and right nodes exist, so no need to check for them. 
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, \
                             p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
    
# NeetCode Solution
# Same idea as me, but did not use recursion. For good reason, too, it just
# looks cleaner.
class NeetCodeSolution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur