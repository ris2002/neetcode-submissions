class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n_min=len(nums)+1
       
        left=0
        n_sum=0
        for right in range(len(nums)):
            n_sum+=nums[right]
 
            while n_sum>=target:
                n_min=min(n_min,(right-left+1))
                n_sum-=nums[left]
                left+=1
            
            
        return n_min if n_min <= len(nums) else 0

        