# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None: return False
        
        walker, runner = head, head
        
        while walker.next is not None and runner.next is not None and runner.next.next is not None: 
            walker, runner = walker.next, runner.next.next
            if walker == runner: return True
            
        return False
    
# walker and runner,good metaphor.
# Walker goes 1 step at a time,and runner goes 2 steps at a time.
# If we think walker is still,then runner goes 1 step at a time.
# So,the problem is just like a Chasing problem.
# There is a time when runner catches walker.
#
# We can make use of [[ Floyd's cycle-finding algorithm ]], also know as tortoise and hare algorithm. 
# The idea is to have two references to the list and move them at different speeds. 
# Move one forward by 1 node and the other by 2 nodes. 
# If the linked list has a loop they will definitely meet.
#
# Time = O(n)
# Space = O(1)