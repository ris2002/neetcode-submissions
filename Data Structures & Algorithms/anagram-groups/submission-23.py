class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n_dict={}
        res=[]
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in n_dict:
                n_dict[sorted_word]=[]
                n_dict[sorted_word].append(word)
            elif sorted_word  in n_dict:
                n_dict[sorted_word].append(word)
        for v in n_dict.values():
            res.append(v)
        return res

    


        