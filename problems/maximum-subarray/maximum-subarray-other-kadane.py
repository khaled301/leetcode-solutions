class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)
    
# Kadane's Algo
### local_maximum[i] = max(A[i], max(A[i], A[i]+local_maximum(A[i-1])) ###  => initial local_maximum = A[0] or A[i-1]
# the purpose of using this algorithm is traverse the array once and make the time complexity O(n)

# where A = [-2,1,-3,4,-1,2,1,-5,4] and first index i = 1;
# So local_maximum[1] = max(A[1], max(A[1], A[1]+local_maximum(A[0]))
#       local_maximum[1] = max(1, max(1, 1+(-2)))
#       local_maximum[1] = max(1, max(1, -1)) = max(1, 1)
# local_maximum[i] = local_maximum[1] = 1

# Likewise  local_maximum[2] = max(A[2], max(A[2], A[2]+local_maximum(A[1]))
#       local_maximum[2] = max(-3, max(-3, -3+1)) => 
#       local_maximum[1] = max(-3, max(-3, -2)) = max(-3, -2)
# local_maximum[i] = local_maximum[2] = -2

# At this point first 3 indices of the array will look like = A = [-2,1,-2  ,    4,-1,2,1,-5,4]
# as the accumulated sum of the A[2] index is negative thus it will not increase the sum 
# and we can skip this A[2] and move the pointer forward(condition in line number #4)
# until we find the positive local_maximum value or hit the end of the list