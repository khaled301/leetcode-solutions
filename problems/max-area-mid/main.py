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

new_sol = Solution()
max_area = new_sol.maxArea([1,8,6,2,5,4,8,3,7])
max_area2 = new_sol.maxArea2([1,1])

print(max_area)
print(max_area2)
