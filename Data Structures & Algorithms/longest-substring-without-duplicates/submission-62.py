class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[]
        left=0
        max_len=0
        n_len=0
        for i in range(len(s)):
            while s[i] in res:
                res.remove(s[left])
                left += 1 
            res.append(s[i])
            n_len=len(res)
            max_len=max(n_len,max_len)
        return max_len


        