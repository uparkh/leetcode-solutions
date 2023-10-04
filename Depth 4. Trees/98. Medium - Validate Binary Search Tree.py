# TOTAL TIME: -3 mins

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


# Could not pass the condition of any node's key being bigger than the left
# subtree, and smaller than the right subtree. 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    # def subTreeRange(self, root: Optional[TreeNode]) -> [int, int]:
        
        # if not root: #     return True # if root.left and root.left.val >= root.val: #     return False # if root.right and root.right.val <= root.val: #     return False

        # if not root:
        #     return [None, None]
        # if root.left:
        #     left_subtree_range = self.subTreeRange(root.left)
        #     if root.left.val >= left_subtree_range[1]ajj
        # if root.right:
        #     right_subtree_range = self.subTreeRange(root.right)
        
        # return self.isValidBST(root.left) and self.isValidBST(root.right)

