from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        
        n = len(nums)
        currentWindow = sum(nums[:k])
        maxSum = currentWindow

        for i in range(n - k):
            currentWindow = currentWindow - nums[i] + nums[i+k]
            maxSum = max(maxSum, currentWindow)
        
        maxAverage = maxSum / k
        return maxAverage
    
solution = Solution() 
print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)) # Output: 12.75
print(solution.findMaxAverage([0,4,0,3,2], 1)) # Output: 04.00