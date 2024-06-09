class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = int(str(x)[::-1])

        return 0 if result > 2**31 - 1 else result * sign