from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # swapping the next nodes' references
            first.next = second.next
            second.next = first
            
            # the below line is super important to connect the previous node with the swapped new node
            # let say nodes connection are like this 2->1->3->4
            # where previous node "prev" or current pointer is in (1) position
            # 3 -> 4 connection needs to be swapped to 4->3
            # As the previous node (1) had the connection (prev.next) with (3) like 1->3
            # We must update this connection with newly swapped node (4)  like this (1->4) 
            # So that the new nodes look like this then 2->1->4->3
            prev.next = second

            # move the prev pointer "just before" the targeted nodes which will be swapped next
            # the position will be act like the dummy position and
            # it is required for the continuity of the connection of the nodes
            prev = first
            
        return dummy.next    