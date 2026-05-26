class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        for char in s:
            if char not in count:
                count[char]=0
            count[char]+=1
        for char in t:
            if char in count:
                count[char]-=1
            if char not in count:
                return False
        for key, val in count.items():
            if count[key]!=0:
                return False
        return True

        
        