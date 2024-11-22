from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, curr = None, head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 
            
        return prev
    
    # input 1-> 3 -> 13 -> None
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or only one node remains
        # Meet the condition at node 13 and returns 13->None as first reversedHead
        if not head or not head.next:
            return head 
        
        # Recursively reverse the rest of the list
        reversedHead = self.reverseList(head.next)
        
        # Make the next node point to the current node
        # after the first reversedHead "13->None" return the "head" will be in node 3->13 in "recursive" call
        # and we need to move the node 3 to the position after the node 13,
        # to look like 13 -> 3 ->... this
        head.next.next = head 
        
        # Break the current node's next pointer to avoid cycles
        # As the node 3 -> has a previous references of node 13, we can set the node 3 ->'s previous reference to None
        head.next = None 
        
        # Return the reversedHead ( 2nd: 13->3->None, 3rd: 13->3->1->None)
        return reversedHead