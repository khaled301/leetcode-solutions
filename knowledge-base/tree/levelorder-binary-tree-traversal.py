
"""
    Problem Leet 102: Given the root of a binary tree, return the level order traversal of its nodes' values.
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # initialize the queue with root node and 
        # result, res with empty list
        queue, res = deque([root]), []
        
        # loop until queue is empty
        while queue:
            # current level size of the queue
            # for instance, initial level size is 1
            lvlSize = len(queue)
            
            # it helps to store the visited nodes values of each level from left to right
            curLvl = []
            
            # loop through the current level size
            for _ in range(lvlSize):
                # dequeue (from the left/beginning) the node from the queue 
                node = queue.popleft()
                
                # append the node value of the current level to the list
                curLvl.append(node.val)

                # append the left node first and then the right node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            # append the current level to the result
            res.append(curLvl)

        return res