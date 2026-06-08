class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n_dict={}
        res=[]
        for word in strs:
         
            sorted_str=tuple((sorted(word)))
            if sorted_str not in n_dict:
                n_dict[sorted_str]=[]
                n_dict[sorted_str].append(word)
            elif sorted_str  in n_dict:
                n_dict[sorted_str].append(word)
        for v in n_dict.values():
            res.append(v)
        return res

        

        