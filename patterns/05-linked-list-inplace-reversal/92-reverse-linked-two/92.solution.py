from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        currentPosition = 0
        dummy = ListNode(0)
        
        # dummy will always point to the head | helps to handle the edge cases
        dummy.next = head
        currentNode = dummy

        while currentNode:
            if (currentPosition + 1) != left:
                currentPosition += 1
                currentNode = currentNode.next
            else:
                beforeLeftNode = currentNode
                leftAsStartNode = currentNode.next
                currentNode = currentNode.next
                currentPosition += 1
                previousNode = None
                
                while currentPosition <= right:
                    next = currentNode.next
                    currentNode.next = previousNode
                    previousNode = currentNode
                    currentNode = next
                    if currentPosition == right:
                        beforeLeftNode.next = previousNode
                        leftAsStartNode.next = next
                    currentPosition += 1
                    
                break
            
        return dummy.next

    # cleaner and easy to understand
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        
        #1) find the node before the left node and reach the left node position
        leftOfPrev, cur = dummy, head
        for i in range(left - 1):
            leftOfPrev, cur = cur, cur.next 
        
        #2) reverse from left to right
        # (R - L + 1) size of the difference and the loop count numbers
        # we have to save the previous node of the left node
        # before starting the below loop, the "leftOfPrev" node will point to the "node before the left node"
        # and the "cur" node will point to the "left node"
        prev = None
        for i in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        #3) update the pointers for the reversed sublist
        # leftOfPrev.next holds the starting "left node" so 
        # we can use the "leftOfPrev.next.next" which is currently None 
        # to point to "cur" which will point to the rest of the nodes after reversal
        leftOfPrev.next.next = cur
        
        # we can now reset the leftOfPrev.next to point to reversed sublist's head
        leftOfPrev.next = prev
        
        return dummy.next
        