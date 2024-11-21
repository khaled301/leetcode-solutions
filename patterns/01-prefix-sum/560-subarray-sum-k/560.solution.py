
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalSubArraysCount = 0
        currentSum = 0
        prefixSumsDict = {0:1} # when current sum equals to k (currentSum == k)

        for num in nums:
            currentSum += num
            print(f"currentSum: {currentSum}")
            diffCurSumK = currentSum - k
            print(f"diffCurSumK: {diffCurSumK}")
            totalSubArraysCount += prefixSumsDict.get(diffCurSumK, 0)
            prefixSumsDict[currentSum] = 1 + prefixSumsDict.get(currentSum, 0)
            print( prefixSumsDict )
            print(f"totalSubArraysCount: {totalSubArraysCount}" )
            print('---')        
        return totalSubArraysCount
    
sol = Solution()
nums = [3, 5, 7, 2]
k = 9
print(sol.subarraySum(nums, k))