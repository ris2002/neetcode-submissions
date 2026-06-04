class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set=set(nums)
        print(num_set)
        n=len(num_set)
        print(n)
        print(len(nums))
        if len(nums)!=n:
            return True
        else:
            return False
        