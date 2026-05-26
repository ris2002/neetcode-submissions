class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #target=num[i]+num[j]+num[k]
        #target-num[k]=num[i]+num[j]
        #target-(num[i]+num[j])=num[k]
        n=len(nums)
        target=0
        count={}
        res=[]
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1

        for i in range(n):
            for j in range(i+1,n):
                third_num=target-(nums[i]+nums[j])
                if third_num in count:
                    if third_num==nums[i]:
                        need_i=1
                    else:
                        need_i=0
                    if third_num==nums[j]:
                        need_j=1
                    else:
                        need_j=0
                    if count[third_num]>=need_i+need_j+1:
                        triplet=sorted([nums[i],nums[j],third_num])
                        if triplet not in res:
                            res.append(triplet)
                    
                        

                            
                    
                    
                        

                    
        return res

                
        