from typing import List
import heapq

class Solution:
    """
        Use BFS with heap. 
        In each iteration, we get the pair with minimal sum and 
        then push its neighboring right and bottom (if exists) into the heap. 
        Repeat k or at most m*n times of such iterations. 
        Time complexity O(k lg k). 
        Space complexity O(k) for the heap.
    """
    def kSmallestPairsWithBFSMinHeap(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n , visited, result = len(nums1), len(nums2), set(), []
        
        if m == 0 or n == 0: return result
        
        heap = [[nums1[0] + nums2[0], (0, 0)]]
        
        for _ in range(min(k, (m * n))):
            sum, (i, j) = heapq.heappop(heap)
        
            result.append([nums1[i], nums2[j]])
            
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], (i + 1, j)])
                visited((i + 1, j))
            
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], (i, j + 1)])
                visited((i, j + 1))
        
        return result
    
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Priority queue (min-heap) to store pairs with smallest sums, sorted by the sum
        heap = []
        
        # Result list to store the pairs
        result = []
        
        # Push the initial and smallest pairs into the priority queue
        for x in nums1:
            heapq.heappush(heap, [x + nums2[0], 0])
        
        while k > 0 and heap:
            # Get the smallest sum and the index of the second element in nums2
            sum, positionInNums2 = heapq.heappop(heap)
            
            # Add the pair to the result list
            result.append([sum - nums2[positionInNums2], nums2[positionInNums2]])
            
            # push the next pair into the priority queue if there are more elements in nums2
            if positionInNums2 + 1 < len(nums2):
                heapq.heappush(heap, [sum - nums2[positionInNums2] + nums2[positionInNums2 + 1], positionInNums2 + 1])
            
            # Decrement k
            k -= 1
        
        # Return the k smallest pairs
        return result
    
    
    # The below solution throws Time Limit Exceeded Error. | Time: O(N^2LogN^2) 
    def kSmallestPairsNonOptimized(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for x in nums1:
            for y in nums2:
                sum = x + y
                heapq.heappush(heap, (sum, [x, y]))
        result = []
        while heap:
            priority, data = heapq.heappop(heap)
            result.append(data)
            # print(f"Popped: sum={priority}, pair={data}")
            if k == len(result):
                break
        return result