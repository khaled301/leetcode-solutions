from typing import Optional 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        right = dummy 
        left = dummy 
        
        for _ in range (n+1):
            if right:
                right = right.next 
        
        while right:
            right = right.next 
            left = left.next 
            
        left.next = left.next.next 
        
        return dummy.next 
    
    
# convert list to linked list
def list_to_linked_list(items):
    dummy = ListNode(0)
    current = dummy 
    
    for item in items:
        current.next = ListNode(item)
        current = current.next 
        
    return dummy.next

def linked_list_to_list(head):
    items = []
    
    while head:
        items.append(head.val)
        head = head.next 

    return items 

# Example usage:
# Test case 1: Input: head = [1,2,3,4,5], n = 2
head = list_to_linked_list([1, 2, 3, 4, 5])
solution = Solution()
new_head = solution.removeNthFromEnd(head, 2)
output = linked_list_to_list(new_head)
print(output)  # Output: [1, 2, 3, 5]


# Test case 2: Input: head = [1], n = 1
head = list_to_linked_list([1])
new_head = solution.removeNthFromEnd(head, 1)
output = linked_list_to_list(new_head)
print(output)  # Output: []

# Test case 3: Input: head = [1,2], n = 1
head = list_to_linked_list([1, 2])
new_head = solution.removeNthFromEnd(head, 2)
output = linked_list_to_list(new_head)
print(output)  # Output: [1]