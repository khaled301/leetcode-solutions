# Linked List In-place Reversal Technique

The Linked List In-place Reversal technique is a powerful approach for solving problems that require modifying or reversing portions of a linked list directly. This technique is widely used in interview problems to reverse sublists or perform specific operations on linked lists efficiently.

---
**Leet Problems**: 206, 92, 24, 143 
---

## **Key Concepts**
- **Inplace Reversal:** Reverses the nodes of a linked list without using extra space for another data structure.
- **Pointer Manipulation:** Rearranges the `next` pointers of the nodes during traversal to reverse the desired section of the list.
- **Sublist Reversal:** Often involves reversing a specific range of nodes in the list while preserving the rest.

---

## **How It Works**

### Step-by-Step Process:
1. **Identify the Range:** Determine the portion of the linked list to reverse.
2. **Traverse and Reverse:**
   - Use pointers to keep track of the current node, previous node, and next node.
   - Reverse the direction of the `next` pointer at each step.
3. **Reconnect:** Reattach the reversed section back to the rest of the list.

---

## **When to Use**
- When a problem requires reversing all or part of a linked list (e.g., Problem 206 - Reverse Linked List).
- When sublists need to be reordered in specific ways (e.g., Problem 92 - Reverse Linked List II).
- To reorder a linked list for other operations, such as merging (e.g., Problem 143 - Reorder List).

---

## **Compute and Update**

### General Inplace Reversal:
1. Use three pointers:
   - `prev` for the previous node.
   - `curr` for the current node.
   - `next` for the next node.
2. Iterate through the range:
   - Update `next` to point to the next node in the list.
   - Reverse the `next` pointer of `curr` to point to `prev`.
   - Move `prev` and `curr` one step forward.

---

## **Examples**

### 1. **Reverse Linked List (Problem 206)**
```python
class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

## Advantages
**Efficiency**: Operates in O(n) time complexity and O(1) space complexity.

**Flexibility**: Applicable for partial or full list reversal, as well as other list reordering tasks.
