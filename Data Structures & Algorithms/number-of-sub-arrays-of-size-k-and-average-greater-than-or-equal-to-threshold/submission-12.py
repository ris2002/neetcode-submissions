class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
       
        sum_x=0
        x=[]
        res=[]
        for i in range(k): 
            sum_x+=arr[i]
            x.append(arr[i])
            if (len(x)==k):
                avg=sum_x/k
                if avg>=threshold:
                    res.append(x)
        for  i in range(k,len(arr)):
            sum_x+=arr[i]
            sum_x-=arr[i-k]
            avg=sum_x/k
            x.append(arr[i])
            
            if avg>=threshold:
                res.append(x)   
            else:
                x.pop(0)
                
        return len(res)

        


            

        