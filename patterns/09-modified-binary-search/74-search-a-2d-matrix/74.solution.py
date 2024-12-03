from typing import List

class Solution:
    def searchMatrixOptimal(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1

        while l <= r:
            mid = l + (r - l) // 2
            mid_row, mid_col = divmod(mid, n)
            
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            self.binarySearch(matrix[0], target)

        left, right = 0, len(matrix) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                return self.binarySearch(matrix[mid], target)
        return False

    def binarySearch(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False