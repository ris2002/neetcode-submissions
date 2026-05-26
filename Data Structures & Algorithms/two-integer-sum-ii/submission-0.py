class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(numbers)):
            s_no=target-numbers[i]
            if s_no in dict:
                return [dict[s_no],i+1]
            dict[numbers[i]]=i+1
        