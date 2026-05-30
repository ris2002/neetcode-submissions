class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        max_num=max(nums)
        min_num=min(nums)
        mid=(max_num+min_num)/2
        lst=[]
        if mid in nums:
            mid+=1

        for i in range(len(nums)):
            a=nums[i]
            
            for j in range(len(nums)-1,-1,-1):
                b=nums[j]
                if j==i:
                    break
                
                l,r=i+1,j-1
                while(l<r):
                    fs=a+b+nums[l]+nums[r]
                    if fs>target:
                        r-=1
                    elif fs<target:
                        l+=1
                    elif fs==target:
                        x=[a,b,nums[l],nums[r]]
                        l+=1
                        r-=1
                        if x not in lst:
                            lst.append(x)
        return lst
                        

            
                


        