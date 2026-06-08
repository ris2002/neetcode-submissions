class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_dict={}
        n=len(nums)
        for num in nums:
            n_dict[num]=n_dict.get(num,0)+1
        for num in nums:
            if n_dict[num]>=(n/2):
                return num
        