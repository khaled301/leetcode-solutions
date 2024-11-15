class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = self.getPrefixSumArray(nums)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 :
            return self.prefixSum[right] - self.prefixSum[left - 1]
        else:
            return self.prefixSum[right]

    def getPrefixSumArray(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i -1]
        return nums
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)