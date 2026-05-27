class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n=len(word1),len(word2)
        i=j=0
        x=""
        if m>n:
            t=i<m
        else:
            t=j<n

        while(t):
            if i<m and j<n:
                x=x+word1[i]
                print('1')
                x=x+word2[j]
                print('2')
                i+=1
                j+=1
            elif i==m or j==n:
                if i==m and j<n:
                    x=x+word2[j]
                    j+=1
                elif j==n and i<m:
                    x=x+word1[i]
                    i+=1
                elif j==n and i==m:
                    break

                    

                
        return x
        
        