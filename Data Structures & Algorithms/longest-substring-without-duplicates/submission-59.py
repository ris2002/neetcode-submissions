class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        s_len=0
        s_max=0
        s_list=[]
        for i in range(len(s)):
           
            while s[i] in s_list:
                s_list.remove(s_list[left])
          
            s_list.append(s[i])
            s_len=len(s_list)
            s_max=max(s_len,s_max)
        return s_max
            
        