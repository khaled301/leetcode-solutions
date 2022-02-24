class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 0,1
        for _ in range(n):
            a,b = b,a+b
        return b
    
# --------------------------------------------------------------------------------------------------------------
# https://youtu.be/Y0lT9Fck7qI
# --------------------------------------------------------------------------------------------------------------
# Dynamic programming - dp[i] = dp[i-1] + dp[i-2] (Similar to Fibonacci series)
# Generalization for any step size - For steps = {1, 3, 5} formula would be dp[i] = dp[i-1] + dp[i-3] + dp[i-5]

# --------------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/climbing-stairs/discuss/861147/Clean-Python-or-Fibonacci-Growth:

# We basically consider all steps from 1 to n: x=[1,2,3,4,...]. 
# Here we note that we can only reach step number x[i] by advancing one step from x[i-1] or 
# two steps from x[i-2]. Based on this insight, we can say with confidence that 
# the total number of alternatives to reach step number x[i] is N[i] = N[i-1]+N[i-2] (sum of alternatives at previous steps). 
# This gives us a Fibonacci growth sequence.

# The steps [i-1] and [i-2] receive the names a and b in the code. 
# If we advance in the array [...,b,a], 
# we can say that new element in the array will be c = a+b. 
# Therefore, we get [..., ,b,a,a+b]. If we iterate in the loop, 
# we note that our variables are updated as b,a = a,a+b, or 
# reversing the order: a,b = a+b,a (this is what appears in the code).

# We return the value of a at the end of the function, 
# because this is our last step taken. Now regarding the initialization a,b=1,0, 
# this can be a bit tricky. 
# One way to sense of this would be to think that initially we are at n=0 (before taking one step), 
# but n=-1 is nonsense, so we have one alternative at n=0 and zero alternatives at n=-1. 
# If you follow the first elements in the sequence [0,1,...], 
# you will see that the upcoming sequence [1,2,3,...] is formed perfectly with this initialization :)

# To be honest, I first thought about this initialization as a small hack to get the code running without if-clauses, 
# because I knew the first element would be c = a+b = 1+0 = 1 for n=1, and then having the initial elements [1,1], 
# the rest of the code would work perfectly lol.