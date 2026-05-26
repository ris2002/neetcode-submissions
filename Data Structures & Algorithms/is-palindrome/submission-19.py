class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence=[]
        s=s.replace(" ","").lower()
        
        x=""
        for char in s:
            if char.isalnum():
                x+=char
        print(x)
        l,r=0,len(x)-1
        while l<r:
            if x[l]==x[r]:
                r-=1
                l+=1
                
            if x[l]!=x[r]:
                return False
            
            
        return True
            