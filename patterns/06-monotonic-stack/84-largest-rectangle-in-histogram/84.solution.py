from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [-1]
        heights.append(-1)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                # stack.pop() is important here instead of stack[-1]
                # because stack[-1] is the index of the current element but
                # we need the index of the previous element in the stack
                # to calculate the distance
                height = heights[stack.pop()]
                
                # to calculate the width aka distance from distB to distA | 4 - 1
                width = i - stack[-1] - 1
                
                maxArea = max(maxArea, (height * width))
                
            stack.append(i)

        return maxArea