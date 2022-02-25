# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        result = []
        stack = deque()
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tempRoot = stack.pop()
                result.append(tempRoot.val)
                root = tempRoot.right
                
        return result