Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Root(3)->Left(9)->Right(20)
Root(9)->Left(Null)->Right(Null)
Root(20)->Left(15)->Right(7)

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


Input: root = [3,9,20,null,null,15,7]
Input: root = [1,null,2]
Input: [1,2,null,3,null,4,null,5]
Input: [2,null,3,null,4,null,5,null,6]
Input: [1,2,3,4,null,null,5]
Input: [3,4,5,-7,-6,null,null,-7,null,-5,null,null,null,-4]