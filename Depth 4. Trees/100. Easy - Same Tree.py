# TOTAL TIME: 7 mins first solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Challenged myself to do a recursive DFS solution first.
from typing import Optional
class RecursiveSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q:  return False
        if p.val != q.val:  return False
        
        # Before this return, we know that p and q:
        # - are non-null
        # - have equal values
        # Thus, we need to check subtrees.
        # Tail-end recursion. I think this gets optimized by the interpreter?
        return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
    
# Iterative DFS solution for fun
class IterativeSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]
        while stack:
            curr_p, curr_q = stack.pop()
            if (not curr_p) ^ (not curr_q): # ^ = xor
                return False
            if curr_p and curr_q:
                if curr_p.val != curr_q.val:
                    return False
                stack.append([curr_p.left, curr_q.left])
                stack.append([curr_p.right, curr_q.right])
        return True


# NeetCode Recursive Solution
# Whereas I single out base cases until the only conclusion is to recurse
# down, NC's solution recurses when the case of valid non-null pointers
# AND equal values is true.
# I **think** mine should be faster? I am not sure if mine counts as tail-end
# or not. I don't think so, I believe for tail-end recursion the last
# statement needs to be a single recursive call, while here to determine
# the last statement two recursive calls need to be evaluated.
# Regardless, the code looks so clean
class NeetCodeSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False