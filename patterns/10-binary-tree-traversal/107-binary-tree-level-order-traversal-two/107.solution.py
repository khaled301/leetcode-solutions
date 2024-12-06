from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottomNonOptimized(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return[]
        
        queue, res = deque([root]), []
        
        while queue:
            size = len(queue)
            lvl = []
            
            for _ in range(size):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(lvl)
            
        res = res[::-1]
        return res



    """

    """
    def levelOrderBottomOptimized(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root, depth, res):
        if root:
            if depth >= len(res):
                res.insert(0, [])
                
            res[-(depth + 1)].append(root.val)
        
            self.dfs(root.left, depth + 1, res)
            self.dfs(root.right, depth + 1, res)
            