class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in range(len(s)):
            for ch in s[i]:
                if ch.isalnum():
                    x+=ch.lower()

               
        print(x)
        left_string=""
        right_string=""
        for i in range(len(x)//2):
            left_string=x[i]
            n=len(x)-1-i
            right_string=x[n]
            if right_string!=left_string:
                return False
        return True

                
        