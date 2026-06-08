class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        n=len(nums)
        while(i<n):
            a=nums[i]
            if a>0:
                break
            
                
            
            left=i+1
            right=n-1
            while(left<right):
                
                threesum=a+nums[left]+nums[right]
                if threesum>0:
                    right-=1
                elif threesum<0:
                    left+=1
                elif threesum==0:
                    x=[a,nums[left],nums[right]]
                    left+=1
                    right-=1
                    if x not in res:
                        res.append(x)
            i+=1
        return res



            
        