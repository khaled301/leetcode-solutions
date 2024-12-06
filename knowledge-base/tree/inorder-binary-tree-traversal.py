
"""
    Problem Leet 94: Given the root of a binary tree, return the inorder traversal of its nodes' values.
    
    1) left -> root -> right
    2) We will maintain a cursor initially pointing to the root and a stack to keep track of the current root node
    3) We will start with the root node and go to the end depth of the left nodes
    4) when the left node is null, we will pop the last root node from the stack 
    5) Append the popped node's value to result
    6) move the cursor to the right node and continue the traversal
    
    7) Time complexity: O(n) as we visit each node once
    8) Space complexity: O(n) 
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack, res = root, [], []
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
                
        return res