class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_dict={}
        x_dict={}
        res_x=[]
        freq_lst=[]
        res=[]
       
        for num in nums:
            n_dict[num]=n_dict.get(num,0)+1
        print(n_dict)
        for key,v in n_dict.items():
            if v not in x_dict:
                x_dict[v]=[]
                x_dict[v].append(key)
            elif v in x_dict:
                x_dict[v].append(key)

        print(x_dict)
       
        for key in x_dict.keys():
            freq_lst.append(key)
        freq_lst.sort()
        g=len(freq_lst)-1
        while( g >= 0):
           
            res_x=res_x+x_dict[freq_lst[g]]
            g-=1
            
        for i in range(k):
            d=res_x[i]
            res.append(d)
        print(res)    
        return res

        
            
        