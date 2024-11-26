from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                tempIndex = stack.pop()
                answer[tempIndex] = i - tempIndex

            stack.append(i)

        return answer