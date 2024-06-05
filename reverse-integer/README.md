# Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
```
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
```

## Optimal Solution Approach:

#### Handling Sign:
sign = 1 if x >= 0 else -1: This line determines the sign of the input integer x. It stores 1 if x is non-negative and -1 if x is negative.

#### Absolute Value:
x = abs(x): The absolute value of x is taken to handle the reversal of digits without worrying about the sign.

#### Reversing Digits:
reversed_x = int(str(x)[::-1]): This is the core of the solution. It converts the absolute value of x to a string, reverses the string using slicing ([::-1]), and then converts the reversed string back to an integer.

#### Overflow Check:
if reversed_x > 2**31 - 1:: This condition checks if the reversed integer reversed_x exceeds the maximum value of a signed 32-bit integer (2^31 - 1).
return 0: If overflow occurs, the function returns 0.

#### Applying Sign:
return sign * reversed_x: Finally, the original sign is applied to the reversed integer using multiplication.

#### Time Complexity: 
O(n), where n is the number of digits in the input integer. The string conversion and reversal take O(n) time.

#### Space Complexity: 
O(n), where n is the number of digits in the input integer. The string conversion and reversal use additional space for the string representation.