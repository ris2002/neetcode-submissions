class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count=defaultdict(list)
        res=[]
        for i in range(len(nums)):
            count[nums[i]].append(i)
        
        for i in range(len(nums)):
            diff=target-nums[i]
            
            if diff in count:
                
                a=count[diff]
                for j in  a:
                    if i!=j:
                        return[i,j]
        
                        
                
      
                
        