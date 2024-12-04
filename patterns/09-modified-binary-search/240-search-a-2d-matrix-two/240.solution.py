from typing import List

class Solution:
    def searchMatrixOptimal(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
    
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True 
            elif target > matrix[i][j]:
                j += 1
            else:
                i -= 1
                
        return False
            
            
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        for mat in matrix:
            if mat[0] <= target and mat[-1] >= target:
                l, r = 0, len(mat) - 1
                
                while l <= r:
                    m = l + (r - l) // 2
                    if mat[m] == target:
                        return True
                    elif target > mat[m]:
                        l = m + 1
                    else:
                        r = m - 1
                        
        return False