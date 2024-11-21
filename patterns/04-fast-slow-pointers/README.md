# Fast And Slow Pointers Technique:

The Fast and Slow Pointers (also known as the Tortoise and Hare) technique is a popular algorithmic method used to detect cycles in data structures such as arrays and linked lists. It employs two pointers that traverse the structure at different speeds to identify patterns or cycles effectively.

**Leet Problems**: (141-Linked List Cycle), (202-Happy Number), (287-Find the Duplicate Number)

## Key Concepts:
**Cycle Detection**: Primarily used to detect cycles in linked lists or arrays.

**Two Pointers**: Utilizes two pointers:
-   A slow pointer that moves one step at a time.
-   A fast pointer that moves two steps at a time.

**Speed Differential**: The different speeds of the pointers allow them to meet at a cycle, if it exists.


## How It Works
**Initialization**: 
Start both fast and slow pointers at the beginning of the data structure.

**Traversal**:
Move the slow pointer by one step.
Move the fast pointer by two steps.

**Detection**:
If there’s a cycle, the fast pointer will eventually meet the slow pointer.
If the fast pointer reaches the end of the data structure, there is no cycle.

**Optional (Cycle Length)**: 
To determine the length of the cycle, keep the fast pointer stationary and move the slow pointer until it returns to the meeting point, counting the steps.

## When to Use
**Cycle Detection in Linked Lists**: 
To determine if a linked list contains a loop

**Detect Repeated States in Computations**: 
Useful for problems involving repetitive states in arrays or mathematical sequences 

**Finding Duplicates in Array Cycles**: 
Efficiently find duplicate elements in a cycle-like structure within an array (e.g., Problem 287 - Find the Duplicate Number).

## Advantages
**Efficiency**: Operates in ***O(n)*** time complexity with ***O(1)*** space, making it highly efficient for large datasets.

**Versatility**: Applicable to a wide range of problems involving cycles in linked lists, arrays, or mathematical sequences.
