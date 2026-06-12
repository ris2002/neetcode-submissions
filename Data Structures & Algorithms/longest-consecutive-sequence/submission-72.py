class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c_max=0
        
        set_nums=set(nums)
        for num in set_nums:
            if num-1 not in set_nums:
                c=1
                while num+c in set_nums:
                    c+=1
                c_max=max(c,c_max)
        return c_max
        