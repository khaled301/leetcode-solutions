# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:   
        response = []
        
        if not root:
            return []
        
        leftValues = self.inorderTraversal(root.left)
        rightValues = self.inorderTraversal(root.right)
        
        response.extend(leftValues)
        response.append(root.val)
        response.extend(rightValues)   

        return response