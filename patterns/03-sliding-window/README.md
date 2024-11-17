# Sliding Window Technique
The sliding window technique is a powerful algorithmic strategy used to solve problems involving arrays or lists. This technique is particularly useful when you need to find a subset of elements that meet certain conditions, such as finding the maximum sum of a subarray of fixed size or detecting a pattern.
It helps to reduce time complexity from O(n * k) to O(n) since we will be using single loop.

**Leet Problems**: 643, 3, 76

## Key Concepts:

### Fixed-Length Sliding Window:
You maintain a window of fixed size and slide it across the array or list.
At each position, you compute the desired property (e.g., sum, maximum) within the window.

### Variable-Length Sliding Window:
The size of the window can change dynamically based on certain conditions.
This is often used in problems where you need to find the longest or shortest subarray that satisfies a given condition.

## How It Works

### Initialization:
Set the starting point of the window.
Initialize variables to store the desired property (e.g., current sum, max sum).

### Slide the Window:
Move the window one element at a time.
Update the window by adding the new element that enters the window and removing the element that exits.

### Compute and Update:
At each position, compute the desired property for the current window.
Update any relevant variables (e.g., max sum, start index).

## When to Use
- To find subarray
- To find substring


## Examples
Find subarray of size 'K' with maximum sum
[3, 2, 7, 5, 9, 6, 2] where K = 2 and N >= 3

### Approach:
-   Initialize the subarray with first 3 elements.
-   Subtract the left most element and add the next element while iterating the main array  
    -   There are always two elements common in the subarray. We subtract the left element and add the following element to reuse the sum and reduce time complexity.

```plaintext
    1) window_sum = 3 + 2 + 7 = 12 ; max_sum = 12; subarray = [3, 2, 7]; initialize the subarray
    2) window_sum = 12 - 3 + 5 = 14 ; max_sum = 14; subarray = [2, 7, 5]; subtract left most element and add the next element
    3) window_sum = 14 - 2 + 9 = 21 ; max_sum = 21; subarray = [7, 5, 9]
    4) window_sum = 21 - 7 + 6 = 20 ; max_sum = 21; subarray = [7, 5, 9]
    5) window_sum = 20 - 5 + 2 = 17 ; max_sum = 21; subarray = [7, 5, 9]
```

### Solution 1:
This solution uses a sliding window with incremental updates. After initially calculating the sum of the first window, it adjusts the window sum by subtracting the element that is sliding out and adding the element that is sliding in.

```python
# Solution 1
def max_subarray_sum_sliding_window(nums, k):
        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum
        max_start_index = 0
        
        for i in range(n - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            
            if window_sum > max_sum:
                max_sum = window_sum
                max_start_index = i + 1
            
        return nums[max_start_index:max_start_index + k], max_sum
    
maxSubarraySum = max_subarray_sum_sliding_window([3, 2, 7, 5, 9, 6, 2], 3)
print(maxSubarraySum)
```

#### Time Complexity: 
𝑂 ( 𝑛 ) for the initial sum calculation and 
𝑂 ( 𝑛 − 𝑘 ) for the sliding adjustments, giving a total complexity of 𝑂 ( 𝑛 )

### Solution 2:
This solution calculates the sum for each window from scratch using slicing and the sum function.

```python
# Solution 2
def max_subarray_sum_sliding_window2(nums, k):
        max_sum = 0
        max_start_index = 0
        
        for i in range((len(nums) - k) + 1):
                window_sum = sum(nums[i:i + k])
                if window_sum > max_sum:
                        max_sum = window_sum
                        max_start_index = i
        return nums[max_start_index:max_start_index + k], max_sum

maxSubarraySum = max_subarray_sum_sliding_window2([3, 2, 7, 5, 9, 6, 10], 3)
print(maxSubarraySum)
```

#### Time Complexity: 
𝑂 ( 𝑘 ) for each sum calculation, repeated 𝑂 ( 𝑛 − 𝑘 ) times, 
giving a total complexity of 𝑂 ( ( 𝑛 − 𝑘 ) × 𝑘 ) .
The use of slicing inside the loop also adds overhead.

### Conclusion
Solution 1 is better because:

#### Efficiency: 
It has a lower time complexity 
𝑂 ( 𝑛 )compared to Solution 2’s 𝑂 ( ( 𝑛 − 𝑘 ) × 𝑘 )
This makes Solution 1 much more suitable for large arrays.

#### Performance: 
The incremental update technique avoids the overhead of repeatedly summing the same elements, 
making it faster in practice.