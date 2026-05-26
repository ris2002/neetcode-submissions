class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count=defaultdict(int)
        for i in range(len(nums)):
            x=nums[i]
            count[x]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in count and count[diff]!=i:
                return [i,count[diff]]