class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        x=[]
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            x=target-nums[i]
            print(x)
            if x in d:
                v=d[x]
                if v!=i:
                    if v<i:
                        return [v,i]
                    else:
                        return [i,v]

                    
                
                    
                
                

        