from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallestNonOptimized(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        res = []
        stack = [(root, False)]

        while stack:
            n, v = stack.pop()
            if n:
                if v:
                    if len(res) < k:
                        res.append(n.val)
                        res.sort()
                    elif n.val < res[-1]:
                        res.pop()
                        res.append(n.val)
                        res.sort()
                else:
                    stack.append((n, True))
                    stack.append((n.right, False))
                    stack.append((n.left, False))

        return res[-1] if res[-1] != float('-inf') else -1
    
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.val)

                if len(res) >= k:
                    break
                
                cur = node.right

        return res[k - 1]
            