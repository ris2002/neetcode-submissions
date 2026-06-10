class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            a=nums[i]
            for j in range(len(nums)-1,-1,-1):
                if j==i:
                    break
                b=nums[j]
                left=i+1
                right=j-1
                while(left<right):
                    x=a+b+nums[left]+nums[right]
                    if x>target:
                        right-=1
                    elif x<target:
                        left+=1
                    elif x==target:
                        lst=[a,b,nums[right],nums[left]]
                        left+=1
                        right-=1
                        if lst not in res:
                            res.append(lst)
        return res

        