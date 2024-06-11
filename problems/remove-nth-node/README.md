Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

# Optimal Solution:

### Dummy Node: 
A dummy node is created and points to the head of the list. This simplifies edge cases such as removing the head of the list.

### Initialize Pointers: 
Two pointers, fast and slow, both start from the dummy node.

### Move Fast Pointer: 
Move the fast pointer n + 1 steps ahead. This ensures that the gap between fast and slow is n number of nodes.

### Move Both Pointers: 
Move both fast and slow pointers one step at a time until fast reaches the end of the list.

### Remove the Target Node: 
The slow pointer will now be just before the node to be removed. Adjust the next pointer of slow to skip the target node.