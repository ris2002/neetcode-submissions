class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = []
        b = []
        for al in s:
            a.append(al)
        for bl in t:
            b.append(bl)
        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] in b:
                    b.remove(a[i])
        if len(b)==0:
            return True
        return False
                
        
        
        
