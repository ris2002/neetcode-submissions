class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        for i in range(len(nums)):
            count[nums[i]]-=1
            if nums[i]==nums[i-1] and i>0:
                
                continue
            for j in range(i+1,len(nums)):
                count[nums[j]]-=1
                if j-1>i and nums[j]==nums[j-1]:
                    
                    continue#above link is to the chat gpt connvo
                target=-(nums[i]+nums[j])#https://www.perplexity.ai/search/class-solution-def-threesum-se-X5bDPFWXQaS.onPgtISFpQ#7
                if count[target]>0:#this is done to make sure there are no duplicates
                    res.append([nums[i],nums[j],target])
               

            #count[target]>0 this is used to identify whether the target is present in the dict or not
                #res.append([nums[i],nums[j],target])
            for j in range(i+1,len(nums)):#This is done so for the next iteraion of i there will be all the elements presrnt
                count[nums[j]]+=1
        return res


            
        