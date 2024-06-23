Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8


## Solution:

- only add open parentheses if open < n
- only add close parentheses if close < open
- valid if open = close = n

### -------------------------------------------------------------------------------

1. total open = n and total closed = n 
2. close < open then add close
3. if open = close then add open if open < n else add only close and close <= n
4. if open = n then add only close and close <= n

### -------------------------------------------------------------------------------
