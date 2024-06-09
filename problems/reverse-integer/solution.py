
class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > (2**31 - 1):
            return 0

        signed = False
        temp = x

        if temp < 0:
            signed = True
            temp = temp * -1
        
        temp = list(reversed(str(temp)))
        temp = int('-' + ''.join(temp) if signed else ''.join(temp))

        if temp < -2**31 or temp > (2**31 - 1):
            return 0

        return temp