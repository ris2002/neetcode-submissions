class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= [[]for i in range(len(nums)+1)]
        count={}
        res=[]
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1
        for key, val in count.items():
            freq[val].append(key)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res

        