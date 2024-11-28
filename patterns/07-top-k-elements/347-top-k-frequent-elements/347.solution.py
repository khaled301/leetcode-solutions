




from typing import List
import heapq

class Solution:
    def topKFrequentUsingMinHeap(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []

        result = []
        record = {}
        heap = []
        
        for num in nums:
            record[num] = 1 + record.get(num, 0)
        
        for key, val in record.items():
            # used tuple to store value and key
            # value here will be the frequency and key will be the number
            # we will push the tuple to the min heap
            # value will be negative to treat it as a max heap because 
            # in min heap the smallest value will be on top, so largest negative value will be on top
            heapq.heappush(heap, (-val, key))
        
        while len(result) < k:
            # we will pop the tuple from the min heap
            # index 1 will be the number from the tuple
            result.append(heapq.heappop(heap)[1])
            
        return result

    # Time Complexity: O(n) | Bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        record = {}

        for num in nums:
            record[num] = 1 + record.get(num, 0)
        for key, val in record.items():
            buckets[val].append(key)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for item in buckets[i]:
                result.append(item)
                if len(result) == k:
                    return result

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
    print(sol.topKFrequent([1], 1)) # [1]
    print(sol.topKFrequent([1,2], 2)) # [1,2]