from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            dummy = ListNode(0)
            dummyHead = None 
            cur = head.next 
            while cur:
                temp = cur
                last = None 
                while temp.next:
                    if not temp.next.next:
                        last = temp.next 
                        temp.next = None
                        break 
                    temp = temp.next
                if last:
                    last.next = cur
                    if not dummy.next:
                        dummyHead = last
                        dummy.next = dummyHead
                        dummyHead = dummyHead.next
                    else:
                        dummyHead.next = last
                        dummyHead = dummyHead.next.next
                cur = cur.next
            if dummy.next:
                head.next = dummy.next
                        