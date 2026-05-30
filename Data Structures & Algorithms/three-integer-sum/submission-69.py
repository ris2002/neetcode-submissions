class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_x=[]
        res=[]
        nums.sort()#compu;sary for 2pointers
        for i,a in enumerate(nums):
            if a>0:
                break # see nums[i] + nums[j] + nums[k] == 0 so one of the numbers must be -ve so we are taking a as -ve no only
            l,r=i+1,len(nums)-1
            while(l<r):
                threesum=a+nums[l]+nums[r]
                if threesum>0:
                    r=r-1
                elif threesum<0:
                    l+=1
                elif threesum==0:
                    x=[a,nums[l],nums[r]]
                    l+=1
                    r-=1
                    if x not in res:
                        res.append(x)
        return res
                
        