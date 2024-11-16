# Two-Pointer Technique
11
15
167
16. 3Sum Closest
18. 4Sum
259. 3Sum Smaller

## Overview
The two-pointer technique is a common algorithmic strategy that uses two indices (pointers) to traverse an array or a string. This technique is particularly useful for solving problems related to searching, sorting, and finding pairs or subarrays that satisfy certain conditions.

## When to Use
- When you need to find pairs in a sorted array that sum up to a target.
- When you need to reverse elements in a subarray or string.
- When you need to find the longest subarray that satisfies certain conditions.
- When you need to merge two sorted arrays.

## Common Patterns
- **Opposite Ends**: Pointers start at the beginning and end of the array and move towards each other.
- **Same Direction**: Both pointers start at the beginning and move towards the end.

## Examples

### Example 1: Two Sum (Opposite Ends)
Given a sorted array, find two numbers that sum up to a specific target.

#### Problem Statement
Given an array of integers `numbers` sorted in non-decreasing order, find two numbers such that they add up to a specific target number. The function `twoSum` should return the indices (1-based) of the two numbers.

#### Python Code
```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
                
        return []

# Example usage
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
print(solution.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # Output: [4, 5]
