from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class DFS:
    def depthFirst(self, root):
        if not root:
            return []
        
        result = []
        stack = deque()
        stack.append(root)
        
        while len(stack) > 0:
            current = stack.pop()
            # print(current.val)
            result.append(current.val)
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                
        return result

        
a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# print(a.val)
# print(a.left)
# print(a.right)

depthFirstValues = DFS()
response = depthFirstValues.depthFirst(a)
print(response)