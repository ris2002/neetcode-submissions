class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left=0
        res=0
        right=len(nums)-1
        mod=1000000007
        while(left<=right):
            if nums[left]+nums[right]>target:
                right-=1
            elif left<=right:
                res+=pow(2,right-left,mod)

                res=res%mod
                left+=1
        return res

        