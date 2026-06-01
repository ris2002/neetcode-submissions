class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(len(nums)-k):
            j=0
           
            while(j<len(nums)-1):
            
                nums[j],nums[j+1]=nums[j+1],nums[j]
                
                j+=1
    
        