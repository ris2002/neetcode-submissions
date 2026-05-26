class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        target = 0
        count = {}
        res = []

        # Build frequency map
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Iterate over all pairs (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                third_num = target - (nums[i] + nums[j])
                if third_num in count:
                    # Determine how many occurrences are needed
                    need_i = 1 if third_num == nums[i] else 0
                    need_j = 1 if third_num == nums[j] else 0

                    # Check if enough occurrences exist
                    if count[third_num] >= need_i + need_j + 1:
                        triplet = sorted([nums[i], nums[j], third_num])
                        if triplet not in res:  # Avoid duplicates
                            res.append(triplet)

        return res