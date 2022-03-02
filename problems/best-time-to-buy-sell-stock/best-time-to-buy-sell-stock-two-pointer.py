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
    
    

        # if not prices or len(prices) == 1:
        #     return 0
        
        # l, r = 0, 1
        # maxProfit = 0
        # for i in range(len(prices)):
        #     if r < len(prices):
        #         if prices[r] > prices[l]:
        #             maxProfit = max((prices[r] - prices[l]) , maxProfit)
        #             r = i+1
        #         else:
        #             l = r
        #             r = l+1

        # return maxProfit