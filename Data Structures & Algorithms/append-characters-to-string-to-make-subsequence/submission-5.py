class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        c=i=j=0
      
        
        while(i<m and j<n):
            if s[i]==t[j]:
                i+=1
                j+=1
            elif s[i]!=t[j]:
                i+=1
        return n-j
            
          
        

