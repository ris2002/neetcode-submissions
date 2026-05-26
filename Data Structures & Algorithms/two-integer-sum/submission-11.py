class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        count={}
        
        for i in range(len(nums)):
            x=nums[i]
            if x not in count:
                count[x]=0
            count[x]=i
        for i in range(len(nums)):
            s_no=target-nums[i]
            if s_no in count and count[s_no]!=i:
                if count[s_no]>i:
                    res.append(i)
                    res.append(int(count[s_no]))
                    break
                else:
                    res.append(int(count[s_no]))
                    res.append(i)
                    break
        return res
                
        