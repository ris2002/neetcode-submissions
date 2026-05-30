class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst=[]
        i=0
        while (i<len(nums)):
            a=nums[i]
            if a>0:
                break
            l,r=i+1,len(nums)-1
            while(l<r):
                threesum=a+nums[l]+nums[r]
                if threesum>0:
                    r=r-1
                elif threesum<0:
                    l=l+1
                elif threesum==0:
                    x=[a,nums[l],nums[r]]
                    if x not in lst:
                        lst.append(x)
                    l+=1
                    r-=1
            i=i+1
        return lst
        
