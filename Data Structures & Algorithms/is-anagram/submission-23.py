class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        
        for str in s:
            
            if str not in count:
                count[str]=0
                
           
            count[str]+=1
        print(count)
        for char in t:
            if char not in count:
                return False
            count[char]-=1
        print(count)
        for key in count.keys():
            if count[key]!=0:
                return False
        return True
        