from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        
        def postOrderMaxGain(node):
            nonlocal maxSum
            
            if not node:
                return 0
            
            leftGain = max(postOrderMaxGain(node.left), 0)
            rightGain = max(postOrderMaxGain(node.right), 0)
            
            currentMaxPath = node.val + leftGain + rightGain
            maxSum = max(maxSum, currentMaxPath)
            
            return node.val + max(leftGain, rightGain)
        
        postOrderMaxGain(root)
        return maxSum
    
    
    def maxPathSumIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack, gains, maxPath = [(root, False)], {}, float('-inf')

        while stack:
            n, v = stack.pop()

            if n:
                if v:
                    leftMaxGain = max(gains.get(n.left, 0), 0)
                    rightMaxGain = max(gains.get(n.right, 0), 0)
                    currentMaxPath = n.val + leftMaxGain + rightMaxGain
                    maxPath = max(maxPath, currentMaxPath)
                    gains[n] = n.val + max(leftMaxGain, rightMaxGain)
                else:
                    stack.append([n, True])
                    stack.append([n.right, False])
                    stack.append([n.left, False])
        
        return maxPath