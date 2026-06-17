class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_count=100001
        nums.sort()
        left=0
        right=k-1
        while(right<len(nums)):
            count=nums[right]-nums[left]
            min_count=min(min_count,count)
            left+=1
            right+=1
        return min_count


        