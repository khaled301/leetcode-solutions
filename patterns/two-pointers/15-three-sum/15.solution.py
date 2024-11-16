class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            # avoid duplicates elem
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                
                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    # avoid duplicates elem
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
                elif curSum > 0:
                    r -= 1
                else:
                    l += 1
        return res