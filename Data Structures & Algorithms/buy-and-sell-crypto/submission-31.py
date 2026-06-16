class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profits=0
        buy=101
        i=0
        n=len(prices)
        while(i<n):
            if (prices[i]<buy):
                buy=prices[i]
                i+=1
            else:
                profits=prices[i]-buy
                max_profits=max(max_profits,profits)
                i+=1
        return max_profits


      

            