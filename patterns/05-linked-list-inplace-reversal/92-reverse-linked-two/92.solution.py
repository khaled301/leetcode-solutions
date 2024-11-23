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
