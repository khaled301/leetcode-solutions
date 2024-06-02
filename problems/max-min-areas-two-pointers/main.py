class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        
        print(len(height))
        
        for i, h in enumerate(height):
            for j, h2 in enumerate(height):
                if i == j:
                    continue
                area = min(h, h2) * (j - i)
                max_area = max(max_area, area)
            
        return max_area

    def maxArea2(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
    def minArea(self, height: list[int]) -> int:
        min_area = float('inf')
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            min_area = min(min_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return int(min_area)


new_sol = Solution()
max_area = new_sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
max_area2 = new_sol.maxArea2([1, 1])
min_area = new_sol.minArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
min_area2 = new_sol.minArea([1, 1])


print(f"Max Area = {max_area}")
print(f"Max Area 02 = {max_area2}")
print(f"Min Area = {min_area}")
print(f"Min Area 02 = {min_area2}")


