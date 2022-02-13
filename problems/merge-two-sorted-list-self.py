# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortLinkedList(self, val, list) -> Optional[ListNode]:
        newNode = ListNode(val, None)
        
        if list is None:
            newNode.next = None
            list = newNode
        elif list.val > val:
            newNode.next = list
            list = newNode
        elif list.val < val and list.next is None:
            list.next = newNode
        else:
            current = list
            while current.next is not None and current.next.val < val:
                current = current.next
            newNode.next = current.next
            current.next = newNode
            
        return list
    
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            while list1.next is not None and list2.next is not None:
                if list1.val < list2.val:
                    newList = self.sortLinkedList(list1.val, newList)
                    list1 = list1.next
                elif list1.val > list2.val:
                    newList = self.sortLinkedList(list2.val, newList)
                    list2 = list2.next
                else: 
                    newList = self.sortLinkedList(list1.val, newList)
                    newList = self.sortLinkedList(list2.val, newList)
                    list1 = list1.next
                    list2 = list2.next    
                    
            while list1 is not None:
                newList = self.sortLinkedList(list1.val, newList)
                list1 = list1.next
                    
            while list2 is not None:
                newList = self.sortLinkedList(list2.val, newList)
                list2 = list2.next
        
        return newList
                