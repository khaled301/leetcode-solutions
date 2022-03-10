from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        singleHash = {}
        
        for i, n in enumerate(nums):
            if n in singleHash:
                del singleHash[n]
            else:
                singleHash[n] = i
    
        return next(iter(singleHash))