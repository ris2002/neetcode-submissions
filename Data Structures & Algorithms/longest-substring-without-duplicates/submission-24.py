class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longest=0
        count_set=set()
        for i in range(len(s)):
            x=s[i]
            while x in count_set:
                count_set.remove(s[left])
                left+=1
            count_set.add(s[i])
            longest = max(longest, i - left + 1)
        return longest
            
                
                
                
        

                

        