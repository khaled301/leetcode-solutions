# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverseTreeForChild(self, root, childTreeDirection=None):        
        if not root:
            return [None]
        
        result = []
        stack = deque()
        stack.append(root)
        
        while len(stack) > 0:
            current = stack.pop()

            if current:
                result.append(current.val)
            else:
                result.append(current)
            
            if childTreeDirection == 'left' and current:
                stack.append(current.right)
                stack.append(current.left)
            elif current:
                stack.append(current.left)
                stack.append(current.right)

        return result

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: True

        leftTreeValues = self.traverseTreeForChild(root, 'left')
        rightTreeValues = self.traverseTreeForChild(root, 'right')

        if leftTreeValues == rightTreeValues: return True
        else: return False