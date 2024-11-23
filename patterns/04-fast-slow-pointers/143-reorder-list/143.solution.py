from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head or head.next:
            slow, fast = head, head.next
            
            # find middle point 
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            # reverse secondReversed half of list
            prev, cur = None, slow 
            while cur:
                next = cur.next 
                cur.next = prev
                prev = cur
                cur = next
            
            # merge two lists
            first,secondReversed = head, prev 
            while first and secondReversed:
                firstNext = first.next
                secondNext = secondReversed.next
                first.next = secondReversed 
                secondReversed.next = firstNext
                secondReversed = secondNext
                first = firstNext

    def reorderList2(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # second portion of the list
        second = slow.next 
        
        # reverse second sublist
        prev = slow.next = None 
        while second:
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp
        
        # merge
        first, second = head, prev 
        while second:
            firstNext, secondNext = first.next, second.next
            first.next = second 
            second.next = firstNext 
            first = firstNext 
            second = secondNext