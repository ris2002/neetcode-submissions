class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        res=0
        nums.sort()
        mod=1000000007
        while(left<=right):
            if nums[left]+nums[right]>target:
                right-=1
                continue
            if left<=right:
                res=res+pow(2,right-left,mod)
                res=res%mod
                left+=1
        return res

        