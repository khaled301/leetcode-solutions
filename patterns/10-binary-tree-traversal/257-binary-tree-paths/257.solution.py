from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfsBTPathFromRoot(node, path, res):
            if not node:
                return
            
            path.append(str(node.val))

            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                dfsBTPathFromRoot(node.left, path, res)
                dfsBTPathFromRoot(node.right, path, res)

            path.pop()
                
        
        res = []
        path = []
        dfsBTPathFromRoot(root, path, res)

        return res
    
    def binaryTreePathsIterative(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        stack = [(root, [str(root.val)])]            

        while stack:
            n, p = stack.pop()

            if not n.left and not n.right:
                res.append("->".join(p))
            if n.left:
                stack.append((n.left, p + [str(n.left.val)]))
            if n.right:
                stack.append((n.right, p + [str(n.right.val)]))
            
        return res
