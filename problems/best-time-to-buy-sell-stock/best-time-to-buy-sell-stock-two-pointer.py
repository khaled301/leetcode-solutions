from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxProfit = 0, 1, 0 # left=buy right=sell max profit = 0
        
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r # shift left pointer to the right pointer as the value at right pointer is lower
            r +=1
            
        return maxProfit
    
# time = O(n)
# space = O(1)