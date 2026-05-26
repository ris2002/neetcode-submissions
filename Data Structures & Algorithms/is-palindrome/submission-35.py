class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=[]
        for a in s:
            if a.isalnum():
                x.append(a.lower())

        print(x)
        n=len(x)
        m=n-1
        i=0
        while i<n:
            if x[i]!=x[m]:
                return False
            i+=1
            m-=1
        return True


        

        