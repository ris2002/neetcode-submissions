class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_dict={}
        buckets=[]
        freq_list=[]
      
        
       
        for num in nums:
            n_dict[num]=n_dict.get(num,0)+1
        print(n_dict)
        for i in range(len(nums)+1):
            buckets.append([])
     
        for key,v in n_dict.items():
            buckets[v].append(key)
        print(buckets)
        for arr in reversed(buckets):
            freq_list=freq_list+arr
        return freq_list[:k]
            