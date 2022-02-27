# Definition for a binary tree node.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traverseTreeForChild(self, root, childTreeDirection=None):
        response = []
        treeValuesFirst = []
        treeValuesSecond = []
        
        if not root: return [None]
        
        if childTreeDirection == 'left':
            treeValuesFirst = self.traverseTreeForChild(root.left, 'left')
            treeValuesSecond = self.traverseTreeForChild(root.right, 'left')
            response.append(root.val)
            response.extend(treeValuesFirst)
            response.extend(treeValuesSecond)
        else:
            treeValuesSecond = self.traverseTreeForChild(root.right, 'right')
            treeValuesFirst = self.traverseTreeForChild(root.left, 'right')
            response.append(root.val)
            response.extend(treeValuesSecond)
            response.extend(treeValuesFirst)
            
        return response
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: True

        leftTreeValues = self.traverseTreeForChild(root, 'left')
        rightTreeValues = self.traverseTreeForChild(root, 'right')

        if leftTreeValues == rightTreeValues: return True
        else: return False
        
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(2)
e = TreeNode(None)
f = TreeNode(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

# print(a.val)
# print(a.left)
# print(a.right)

depthFirstValues = Solution()
response = depthFirstValues.isSymmetric(a)
print(response)