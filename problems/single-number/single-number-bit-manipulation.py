from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleNumber = 0
        
        for n in nums:
            singleNumber = n ^ singleNumber
        return singleNumber
    
# XOR = (Exclusive OR) = here zero can not change the result
# 56 ^ 56 = 0
# 0 ^ 56 = 56
# 1 ^ 0 = 1
# 1 ^ 1 = 0
# 0 ^ 0 = 0

# [
    # 4 = 100
    # 1 = 001
    # 2 = 010
    # 1 = 001
    # 2 = 010
# ]