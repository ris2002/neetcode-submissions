class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        window=0
        base=0
        n=len(customers)
        for i in range(n):
            if grumpy[i]==0:
                base+=customers[i]
        for i in range(minutes):
            if grumpy[i]==1:
                window+=customers[i]
        maax=window
        for i in range(minutes,n):
            if grumpy[i]==1:
                window+=customers[i]
            if grumpy[i-minutes]==1:
                window-=customers[i-minutes]
            maax=max(maax,window)
        return maax+base

        