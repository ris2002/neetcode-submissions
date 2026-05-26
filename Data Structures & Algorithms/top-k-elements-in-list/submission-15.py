class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = 0
        dict = {}
        freq=[]
        for num in nums:
            if num not in dict:
                dict[num] = 0
        print(dict)

        for num in nums:
            if num in dict:
                dict[num] = dict[num] + 1
        print(dict)

        while len(freq)<k:
            max_val=0
            max_key=None
            for key,val in dict.items():
                if val>max_val:
                    max_key = key
                    max_val =val
            freq.append(max_key)
            del dict[max_key]               

        return freq
