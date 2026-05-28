class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m,n=len(nums1),len(nums2)
        
        k=i=j=0
        nums=[]
        while(k<m-n):
            nums.append(nums1[k])
            k=k+1
            
        numsx=[]
        p=len(nums)
        
        while (i<p or  j<n):
            if i<p and  j<n:
                if nums[i] > nums2[j]:
                    print(nums2[j])
                    numsx.append(nums2[j])
                    j+=1
                elif nums[i] < nums2[j]:
                    numsx.append(nums[i])
                    print(nums[i])
                    i+=1
                elif nums[i]==nums2[j]:
                    numsx.append(nums[i])
                    numsx.append(nums[i])
                    
                    i+=1
                    j+=1
            elif i<p or  j<n:
                if i<p and j==n:
                    numsx.append(nums[i])
                    i+=1
                elif j<n and i==p:
                    numsx.append(nums2[j])
                    j+=1 
        print(numsx)
        for i in range(len(nums1)):
            nums1[i]=numsx[i]

        
        
        