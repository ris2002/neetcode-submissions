class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        skip=[]
        res=[]
       

        for i in range(n):
            if i in skip:
                continue
            n_dict={}
            lst=[]
           
            word=strs[i]
            lst.append(word)
            for char in word:
                n_dict[char]=n_dict.get(char,0)+1
            print(n_dict)
            for j in range(i+1,n):
                x_word=strs[j]
                x_dict={}
                for char in x_word:
                    x_dict[char]=x_dict.get(char,0)+1
                if x_dict==n_dict:
                    lst.append(x_word)
                    skip.append(j)
                else:
                    continue
            res.append(lst)
        return(res)

       
        
            

        
           