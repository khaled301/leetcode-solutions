class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashIndexMapStore = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in hashIndexMapStore:
                return [hashIndexMapStore[diff], i]
            hashIndexMapStore[n] = i
        return