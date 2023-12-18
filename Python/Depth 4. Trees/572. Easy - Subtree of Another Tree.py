# TOTAL TIME: ??m, ??s
# Forgot to track it this time 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Original Solution - O(m*n)
# Was trying to make it O(m + n), but couldn't quite connect the pieces to
# track the last offending node when doing isSameTree check.
from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) if root.left else False)\
            or (self.isSubtree(root.right, subRoot) if root.right else False)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    # My attempt at making this an O(n) solution instead of an O(n^2) solution
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> [bool, TreeNode, TreeNode]:
    #     if not p and not q:
    #         return [True, None, None]
    #     if p and q and p.val == q.val:
    #         left_info = self.isSameTree(p.left, q.left) 
    #         right_info = self.isSameTree(p.right, q.right)

    #     else:
    #         return [False, p, q]

# NeetCode Solution - O(m*n)
# Same idea/fundamental structure as my original solution,
# just has cleaner processing of the False cases.
# I realize now that an empty/null subtree is a part of every tree,
# but an empty main tree has no subtrees besides null ones,
# so those can be ruled out.
class NeetCodeSolution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False 