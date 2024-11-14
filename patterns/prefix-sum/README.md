# Prefix Sum Calculation
Query sum of elements in a sub-array

## Problem
Given an array `A`, efficiently compute the sum of any subarray `A[i]` to `A[j]`.

## Prefix Sum Array
Define the prefix sum array `P` as:
```plaintext
P[i] = A[0] + A[1] + ... + A[i]
```

To calculate the sum from index i to j, use
```plaintext
Sum[i, j] = P[j] - P[i - 1]
```

## Why P[i - 1] and not P[i]?
Using P[i - 1] allows us to exclude all elements before index i, so the sum includes elements from i through j only.
If we subtracted P[i] instead, we would exclude A[i] itself, giving an incorrect sum.

In short, the P[i] includes the value of Array at index i which we need to calculate the sum.

## Example
Given A = [2, 4, 6, 8, 10]:

- Prefix Sum Array P:
```plaintext
A = [2, 4, 6, 8, 10]

P[0] = 2
P[1] = 2 + 4 = 6
P[2] = 2 + 4 + 6 = 12
P[3] = 2 + 4 + 6 + 8 = 20
P[4] = 2 + 4 + 6 + 8 + 10 = 30

Therefore, P = [2, 6, 12, 20, 30]

```

- Range Sum Calculation: For i = 1, j = 3 (sum of A[1] to A[3]):
```plaintext
Sum[1, 3] = P[3] - P[0] = 20 - 2 = 18
```
Answer: 18

```bash
def create_prefix_sum(arr):
    sum = 0
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr 