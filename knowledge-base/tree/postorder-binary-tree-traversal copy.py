
"""
    Problem Leet 145: Given the root of a binary tree, return the post traversal of its nodes' values.
    
    1) [left -> right -> root]
    
    2) Not it is similar to the reverse of the preorder traversal
    3) So the trick would be to do the preorder traversal and reverse the result
    4) Only catch is that we have to store the left node in the stack instead of the right node
    5) And traverse the right node before the left node
    6) At the end, reverse the result
    
    7) Think of it as "Root -> Right -> Left" and reverse it to get "Left -> Right -> Root" (final result)
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack, res, visited = root, [], [], []

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()

        res = res[::-1]
        return res