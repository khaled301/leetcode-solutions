class Solution:
    def isHappy1(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
    
    def isHappy2(self, n: int) -> bool:
        def sumOfSquares(num):
            return sum(int(digit) ** 2 for digit in str(num))

        slow = n
        fast = sumOfSquares(n)
        while fast != 1 and slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        return fast == 1