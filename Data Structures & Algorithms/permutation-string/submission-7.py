class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        str_1=[]
        x_1=[]
        if len(s1)>len(s2):
            return False
        for char in s1:
            str_1.append(char)
        for i in range(k):
            x_1.append(s2[i])
            if len(x_1)==len(str_1):
                a_1=sorted(x_1)
                b_1=sorted(str_1)
                if a_1==b_1:
                    return True
        for i in range(k,len(s2)):
            x_1.pop(0)
            x_1.append(s2[i])
            if len(x_1)==len(str_1):
                
                if len(x_1)==len(str_1):
                    a_1=sorted(x_1)
                    b_1=sorted(str_1)
                    if a_1==b_1:
                        return True
        return False
                

            
            
        