
from typing import List

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = nums[:k]
#         heapq.heapify(heap)
        
#         for num in nums[k:]:
#             if num > heap[0]:
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, num)
        
#         return heap[0]

class HeapQ:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def heapifyDown(self, idx, n):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        
        if left < n and self.nums[left] < self.nums[smallest]:
            smallest = left
            
        if right < n and self.nums[right] < self.nums[smallest]:
            smallest = right

        if smallest != idx:
            self.nums[idx], self.nums[smallest] = self.nums[smallest], self.nums[idx]
            self.heapifyDown(smallest, n)

    def heapifyUp(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.nums[idx] < self.nums[parent]:
            self.nums[idx], self.nums[parent] = self.nums[parent], self.nums[idx]
            idx = parent
            parent = (idx - 1) // 2
        
    def heapify(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapifyDown(i, self.size)
            
    def heappop(self):
        if len(self.nums) == 0:
            return None
        
        smallestItem = self.nums[0]
        self.nums[0] = self.nums[-1]
        self.nums.pop()
        self.heapifyDown(0, len(self.nums))
        
        return smallestItem
    
    def heappush(self, num):
        self.nums.append(num)
        self.heapifyUp(self.size - 1)
    
class Solution:
    # Input: nums = [3,2,1,5,6,4], k = 2
    # # Output: 5

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapQ = HeapQ(heap)
        heapQ.heapify()
        
        for num in nums[k:]:
            if num > heap[0]:
                heapQ.heappop()
                heapQ.heappush(num)
        
        return heap[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))
    print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))