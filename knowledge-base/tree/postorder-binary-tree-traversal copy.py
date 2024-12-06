

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, visited, res = [root], [False], []

        while stack:
            cur, v = stack.pop(), visited.pop()
            
            # When the current popped node is not None 
            # for child node the two left and right nodes can be None
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    # 03 - we have to pop the parent node last (L - > R - > [Root]) from the stack Stack
                    stack.append(cur)
                    
                    # here we mark the current node as visited because 
                    # it is the popped node from the top of the stack
                    # and we don't want to visit it again
                    visited.append(True)
                    
                    # 02 - we have to pop the right node second (L - > [R] - > Root) from the stack Stack
                    stack.append(cur.right)
                    visited.append(False)
                    
                    # 01  - we have to pop the left node first ([L] - > R - > Root) from the stack Stack  
                    stack.append(cur.left)
                    visited.append(False)
                
        return res
    
    """
        Problem Leet 145: Given the root of a binary tree, return the post traversal of its nodes' values.
        
        1) Postorder[left -> right -> root] traversal
        
        2) Note that this traversal is similar to the reverse of the "preorder (Root -> Left -> Right)" traversal 
        
        3) So the trick would be to do the preorder traversal and reverse the result
        4) Only catch is that we have to store the left node in the stack instead of the right node
        5) And traverse the right node before the left node
        6) At the end, reverse the result
        
        7) Think of it as "Root -> Right -> Left" and then reverse it to get the original form "Left -> Right -> Root" (final result)
    """
    def postorderTraversalWithTrick(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack, res = root, [], []

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()

        res = res[::-1]
        return res
    
    
    # without using stack
    def postorderTraversalWithoutTrick(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack, res = root, [], []

        while cur or stack:
            
            # traverse the end of the left child nodes
            if cur:
                stack.append(cur)
                cur = cur.left
            
            # when the current node has no left child
            else:
                
                # check if the current node or the top of the stack has a right child
                # if so go to the right child because (left ->  right -> root)
                # if no left, look for right child and then process the root/parent
                if stack[-1].right:
                    cur = stack[-1].right
                
                # when the current node has no right child
                else:
                    
                    # pop the top of the stack as it will be end node with no right or left nodes
                    temp = stack.pop()
                    
                    # process and append the node value into the result
                    res.append(temp.val)

                    # check if the right node of the top of the stack is the same as the current node
                    # if so, keep popping the top of the stack and append the node value to result until 
                    # the condition doesn't hold or the stack is empty
                    # 
                    # This is required to process the parent node as after we skipped the parent node 
                    # and move to the right node after processing the left node
                    # So if the temp node will only be equal to the right node of the top of the stack
                    # when top of the stack node is the parent node of the popped out right node
                    # as a result we will be sure that we don't need to process the parent node
                    # and we can popped the parent node from the stack and append it to the result
                    while stack and stack[-1].right == temp:
                        temp = stack.pop()
                        res.append(temp.val)

                    # if the stack is not empty and 
                    # top of the stack (parent node) has a unprocessed right child
                    if stack and stack[-1].right:
                        cur = stack[-1].right

        return res