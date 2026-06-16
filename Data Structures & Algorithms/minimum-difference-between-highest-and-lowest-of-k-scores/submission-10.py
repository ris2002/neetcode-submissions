class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        array=[]
        min_count=100001
       
        left=0
        right=k-1
     
        while(right<len(nums)):
            diff=nums[right]-nums[left]
            min_count=min(min_count,diff)
            left+=1
            right+=1

            
        return min_count

        