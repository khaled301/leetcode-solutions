
"""
    Problem Leet 144: Given the root of a binary tree, return the preorder traversal of its nodes' values.
    
    1) root -> left -> right
    2) We will maintain a cursor initially pointing to the root and a stack to keep track of the right node
    3) We will start with the root node and go to the depth of the left nodes and store each left node in the result
    4) when the left node is null, we will pop the right node from the stack 
    5) and continue the traversal of the right node until
    6) the both cursor and stack are empty
    7) Time complexity: O(n) as we visit each node once
    8) Space complexity: O(n) as we store each node in the result or Log(n) if the tree is balanced binary tree
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cursor, stack, result = root, [], []

        while cursor or stack:
            if cursor:
                result.append(cursor.val)
                stack.append(cursor.right)
                cursor = cursor.left
            else:
                cursor = stack.pop()
        
        return result