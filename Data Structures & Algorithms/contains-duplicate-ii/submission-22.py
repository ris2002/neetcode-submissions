class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n_dict=defaultdict(list)
        for i in range(len(nums)):
            n_dict[nums[i]].append(i)
        print(n_dict)
        for key in n_dict.keys():
            val=n_dict[key]
            if len(val)>1:
                
                i=0
                while i<len(val)-1:
                    sub=abs(val[i]-val[i+1])
                    if sub<=k:
                        return True
                    i+=1
                
                    
                
                    
                    
            else:
                continue

        return False

        