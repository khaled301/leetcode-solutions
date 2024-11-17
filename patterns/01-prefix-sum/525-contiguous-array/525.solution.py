class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones,zeros = 0, 0
        max_length = 0
        
        diff_index = {} # count[1] - count[0] -> index
        
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1
                
            if ones - zeros not in diff_index:
                diff_index[ones - zeros] = i 
            
            if ones == zeros:
                max_length = ones + zeros  
            else:
                idx = diff_index[ones - zeros]
                max_length = max(max_length, i - idx)
                
        return max_length