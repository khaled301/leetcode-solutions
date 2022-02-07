# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListLength = len(lists) 
        mergedList = []
        FinalList = None
        
        if ListLength < 1:
            return ListNode('')
        if ListLength == 1:
            return lists[0]
        
        for i, n in enumerate(lists):
            TempNode = n
            
            if TempNode is None:
                continue
            elif TempNode.next is None:
                mergedList.append(TempNode.val)
                continue
            
            while TempNode.next:
                mergedList.append(TempNode.val)
                
                if TempNode.next.next is None:
                    mergedList.append(TempNode.next.val)
                    
                TempNode = TempNode.next 

        mergedList = sorted(mergedList, reverse=True) 

        for i, n in enumerate(mergedList):
            TempFinalList = ListNode(n)
            
            if FinalList is None:
                FinalList = TempFinalList
            else:
                TempFinalList.next = FinalList
            
            FinalList = TempFinalList
        
        return FinalList