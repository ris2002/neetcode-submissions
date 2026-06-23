class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base=0
        x_sum=0
        
        n=len(customers)
        for i in range(n):
            if grumpy[i]==0:
                base+=customers[i]
        for i in range(minutes):
            if grumpy[i]==1:
                x_sum+=customers[i]
        max_sum=x_sum
        for i in range(minutes,n):
            if grumpy[i]==1:
                x_sum+=customers[i]
            if grumpy[i-minutes]==1:
                x_sum-=customers[i-minutes]
            max_sum=max(max_sum,x_sum)
        return max_sum+base
        
        
        