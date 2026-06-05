class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        for char in s:
            s_dict[char]= s_dict.get(char, 0)+1
        for char in t:
            t_dict[char]=t_dict.get(char, 0)+1
        if len(s)!=len(t):
            return False
        for char in s:
            if char in s_dict and char in t_dict:
                    if s_dict[char]!=t_dict[char]:
                        return False
                    
            else:
                return False
        return True
                    