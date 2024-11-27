# Top 'K' Elements Technique

A **monotonic stack** is a data structure that maintains its elements in either increasing or decreasing order. It is commonly used to solve problems involving the **next greater element**, **next smaller element**, or related queries efficiently.

---
**Leet Problems**: 496, 739, 84

---
### Types of Monotonic Stacks

1. **Increasing Monotonic Stack**:
   - The elements in the stack are in increasing order (top of the stack has the largest element).
   - Used to find the next smaller element or handle non-decreasing sequences.

2. **Decreasing Monotonic Stack**:
   - The elements in the stack are in decreasing order (top of the stack has the smallest element).
   - Used to find the next greater element or handle non-increasing sequences.

---

## **Key Concepts**

- Efficiently reduces redundant comparisons by maintaining order.
- Guarantees that each element is pushed and popped at most once, ensuring `O(n)` time complexity.

---

## **How It Works**


1. **Iterate Through the Array**:
   - Traverse each element of the array one by one.

2. **While Condition**:
   - Use a `while` loop to check the stack.
   - Compare the current element with the top of the stack. If it satisfies the monotonic condition (greater or smaller), pop elements from the stack.

3. **Update Result**:
   - If the current element is the next greater or smaller for the top of the stack, update the result accordingly.

4. **Push the Current Element**:
   - After processing, push the current element (or its index) onto the stack.

5. **Handle Remaining Elements**:
   - If any elements remain in the stack, they do not have a valid "next" element, and their result remains as per initialization (e.g., `-1`).

---

## **When to Use**
- Finding **next greater element** (decreasing stack).
- Finding **next smaller element** (increasing stack).
- Solving problems like **largest rectangle in histogram**, **daily temperatures**, and more.

---

## **Compute and Update**

### General Inplace Reversal:
1. 

---

## **Examples**

### Solution 1. Brute Force (Not good)

Time complexity would be O(n^2) for the below solution

```python
def nextGreaterElement(arr):
   n = len(arr)
   result = [-1] * n

   for i in range(n):
      for j in range(i + 1, n):
         if arr[i] < arr[j]:
            result[i] = arr[j]
            break

   return result
```

### Solution 2. 
```python
def nextGreaterElement(arr):
   n = len(arr)
   result = [-1] * n 
   stack = []
   
   for i in range(n):
      while stack and arr[i] > arr[stack[-1]]:
         result[stack.pop()] = arr[i]

      stack.append(i)

   return result
```

The `nextGreaterElement` function finds the next greater element for each element in an array. If no such element exists, it returns `-1` for that position.

## Algorithm Overview

1. **Initialize Variables**:
   - `result`: An array of size `n` initialized to `-1`.
   - `stack`: An empty stack to keep track of indices.

2. **Iterate Through the Array**:
   - For each element, check the stack.
   - If the current element is greater than the element at the index stored on top of the stack, update the `result` for that index and pop it from the stack.
   - Push the current index onto the stack.

3. **Return Result**:
   - At the end, any indices left in the stack will remain `-1` in the `result`, as no greater element exists for them.

---

## Simulation Table

| Step | `i` | `arr[i]` | Stack (Index) | Stack (Values)       | `result`                | Action                           |
|------|-----|----------|---------------|----------------------|-------------------------|----------------------------------|
| 1    | 0   | 4        | [0]           | [4]                  | [-1, -1, -1, -1]        | Push index 0 onto the stack     |
| 2    | 1   | 5        | []            | []                   | [5, -1, -1, -1]         | Pop index 0, update `result[0]` |
| 3    | 1   | 5        | [1]           | [5]                  | [5, -1, -1, -1]         | Push index 1 onto the stack     |
| 4    | 2   | 2        | [1, 2]        | [5, 2]               | [5, -1, -1, -1]         | Push index 2 onto the stack     |
| 5    | 3   | 7        | [3]           | [7]                  | [5, 7, 7, -1]           | Pop indices 2, 1, update `result` |
| 6    | End | -        | [3]           | [7]                  | [5, 7, 7, -1]           | No further elements to process  |

---

## Explanation of the Simulation

1. **Step 1**:
   - Current element: `4`
   - Stack is empty, so push index `0`.
   - No updates to the result array.

2. **Step 2**:
   - Current element: `5`
   - It is greater than `4` (element at index `0` in the stack).
   - Pop index `0`, update `result[0] = 5`.
   - Push index `1`.

3. **Step 3**:
   - Current element: `2`
   - It is not greater than `5` (element at index `1` in the stack).
   - Push index `2`.

4. **Step 4**:
   - Current element: `7`
   - It is greater than `2` (element at index `2`) and `5` (element at index `1`).
   - Pop indices `2` and `1`, update `result[2] = 7` and `result[1] = 7`.
   - Push index `3`.

5. **End**:
   - No more elements to process. The remaining index `3` in the stack has no greater element, so `result[3]` remains `-1`.

---

## Final Result

The `result` array after processing is: `[5, 7, 7, -1]`


## Time and Space Complexity

- **Time Complexity**: `O(n)`  
  Each element is pushed and popped from the stack exactly once, resulting in a linear time complexity.

- **Space Complexity**: `O(n)`  
  The stack can hold at most `n` indices in the worst case, giving a linear space complexity.
