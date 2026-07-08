class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxProfit=0
        for i in range(0,n-1,1):
            for j in range(i+1,n,1):
                profit=prices[j]-prices[i]
                maxProfit=max(maxProfit,profit)
        
        return maxProfit
        