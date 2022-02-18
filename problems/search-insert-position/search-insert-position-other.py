from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) < 1: return 0
        else:
            l, r = 0, len(nums)-1
            
            while r >= l:
                mid = (r+l)//2
                
                if nums[mid] == target: return mid 
                elif nums[mid] > target: r = mid-1
                else: l = mid+1
                
            return l
        
# x = 10
arr = [ 2, 4, 6, 8, 10, 12 ]
# x = 3
x = 5
# arr = [ 1, 3 ]
# x = 0

# Function call
solution = Solution()
result = solution.searchInsert(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    
    
# Here important point to remember is that why we are returning left pointer value
# if no match is found.
# So if no match is found then will be left with only one index. 
# Now in that if the target is greater than the value of the list on that index then
# while loop will break for left pointer value (l+1) which valid result
# on the other hand, while loop will also break if the target is less than the value on that index
# because in that case right pointer will be less than left pointer right < left. Even in that scenario
# left pointer will be the valid index value
# nums = [2] and target is 3 ==> while loop break =>( r = 0, left = 1, mid = 0) as 3 > 2
# nums = [2] and target is 1 ==> while loop break =>( r = -1, left = 1, mid = 0) as  2 > 1