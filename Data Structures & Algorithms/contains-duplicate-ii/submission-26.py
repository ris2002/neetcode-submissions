class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L=0
        window_set=set()
        L=0
        for R in range(len(nums)):
            if abs(R-L)>k:
                window_set.remove(nums[L])
                L+=1
            if nums[R] in window_set:
                return True
            window_set.add(nums[R])
        return False
        