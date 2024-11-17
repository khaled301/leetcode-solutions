
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalSubArraysCount = 0
        currentSum = 0
        prefixSumsDict = {0:1} # when current sum equals to k (currentSum == k)

        for num in nums:
            currentSum += num
            diffCurSumK = currentSum - k
            totalSubArraysCount += prefixSumsDict.get(diffCurSumK, 0)
            prefixSumsDict[currentSum] = 1 + prefixSumsDict.get(currentSum, 0)
        
        return totalSubArraysCount