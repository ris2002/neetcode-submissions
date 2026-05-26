class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=list(set(nums))
        longest=0
        for num in nums:
            if num-1 not in nums:
                #setting the 1st element
                length=1
                while num+length in nums:
                    length+=1
                longest=max(length,longest)
                
            
        return longest




        