class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count=defaultdict(int)
        n=len(numbers)
        for i  in range(n):
            num=numbers[i]
            count[num]=i
            
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in count:
                j=count[diff]
                if j!=i:
                    return[i+1,j+1]


        