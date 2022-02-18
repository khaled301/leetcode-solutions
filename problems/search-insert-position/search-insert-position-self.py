from typing import List

class Solution:
    def findIndexUsingBinarySearch(self, nums: List[int], low, high, target: int) -> int:
        if high >= low:
            mid = (high+low)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.findIndexUsingBinarySearch(nums, mid+1, high, target)
            else:
                return self.findIndexUsingBinarySearch(nums, low, mid-1, target)
        else:
            if low >= 0 and low <= len(nums)-1:
                if nums[low] > target:
                    return low
                else:
                    return low+1
            else:
                return low
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return 0
        else:
            return self.findIndexUsingBinarySearch(nums, 0, len(nums)-1, target)
        
        

# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
# arr = [ 2, 4, 6, 8, 10, 12 ]
# x = 3
# x = 5
arr = [ 1, 3 ]
x = 0

# Function call
solution = Solution()
result = solution.searchInsert(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    
    
# Use return for recursive function in order to put its value into the stack , 
# so that when function will do recursion values from the stack are taken one by one. 
# If you don't use return , the stack will collect only "None" values.