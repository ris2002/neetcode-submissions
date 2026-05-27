class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m,n=len(word),len(abbr)
        i=j=0
        
        
        while(i<m and j<n):
            if word[i]==abbr[j]:
                i+=1
                j+=1
           
            elif word[i]!=abbr[j]:
                
                if abbr[j].isalpha() or abbr[j]=='0':
                    return False

                sLen=0
                while(j<n):
                    
                    if abbr[j].isdigit():
                        sLen=sLen*10+int(abbr[j])
                        j+=1
                    else:
                        break
                i+=sLen
             
        return i==m and j==n
                    

        