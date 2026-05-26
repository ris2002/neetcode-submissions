class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP=0
        while r<len(prices):
            print("l",l)
            print("r",r)
            print("prices[l]=",prices[l])
            print("prices[r]=",prices[r])
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                
                maxP=max(maxP,profit)
                print("max",maxP)
            else:
                l=r
            r+=1
        return maxP
        