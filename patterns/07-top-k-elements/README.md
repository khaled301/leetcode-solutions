# Top 'K' Elements Technique

The "Top 'K' Elements" technique is a common pattern used in algorithmic problems to find the largest or smallest `K` elements from a dataset. This is efficiently achieved using a **heap (priority queue)** due to its ability to dynamically maintain the order of elements during insertion and removal.

---

**Leet Problems**: 215, 347, 373

---


## Why Use a Heap?

Heaps are ideal for "Top K" problems because:
1. **Efficiency**: Inserting and removing elements in a heap takes \(O(log k)\) time.
2. **Dynamic Nature**: A heap can dynamically maintain the top `K` elements during traversal or processing of the input.

---

## Concept
The technique involves:
1. Using a **Min-Heap** to find the `K` largest elements.
2. Using a **Max-Heap** to find the `K` smallest elements.
3. Restricting the heap size to `K`, ensuring that:
   - The root of the heap always represents the smallest or largest of the `K` elements.

---

## General Steps
1. **Choose the Heap Type**:
   - Use a Min-Heap for finding the largest `K` elements.
   - Use a Max-Heap for finding the smallest `K` elements.

2. **Iterate Over the Input**:
   - For each element, add it to the heap.
   - If the heap size exceeds `K`, remove the root (the smallest/largest).

3. **Extract the Results**:
   - The heap contains the desired `K` elements, either in sorted or unsorted order.

---

## Example Problems

### Problem 1: Find the `K` Largest Elements
Given an array `nums` and an integer `K`, return the `K` largest elements.

#### Algorithm
1. Use a Min-Heap of size `K`.
2. Iterate through the array:
   - Add each element to the heap.
   - If the heap size exceeds `K`, remove the smallest element (heap root).
3. The heap contains the `K` largest elements.

#### Code
```python
import heapq
from typing import List

def findKLargest(nums: List[int], k: int) -> List[int]:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove the smallest element
    return list(heap)

