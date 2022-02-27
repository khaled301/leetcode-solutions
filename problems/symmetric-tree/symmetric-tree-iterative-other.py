# Definition for a binary tree node.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False 
            elif left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
            
        return True
    
# When both left and right equals to None, it doesn't mean we have checked every node in the tree, 
# so we use 'continue' to keep the while loop going.
# If we 'return True' at that point, our stack might not be empty yet, 
# which means there are still nodes we haven't checked, so we might have the wrong answer.