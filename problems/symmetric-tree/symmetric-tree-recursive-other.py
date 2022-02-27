# Definition for a binary tree node.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True 
        elif left is None or right is None:
            return False
        elif left.val == right.val:
            leftChildFirst = self.isMirror(left.left, right.right)
            rightChildFirst = self.isMirror(left.right, right.left)
            
            return leftChildFirst and rightChildFirst
        else:
            return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: True
        else: return self.isMirror(root.left, root.right)
