from typing import List

class Solution:
    # using set
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return nums[i]
            visited.add(nums[i])
            
    # using fast and slow (two) pointers
    def findDuplicate2(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        print(f'Initial => slow: {slow}, fast: {fast}')
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print(f'Before => slow: {slow}, fast: {fast}')
    
        return fast
    

sol = Solution()
# nums = [1,3,4,2,2]
nums = [2,1,3,4,3]
print(sol.findDuplicate2(nums))