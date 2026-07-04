class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n_dict=defaultdict(int)
        left=0
        n_max=0
        for right in range(len(s)):
            n_dict[s[right]]+=1
            while (right-left+1)-max(n_dict.values())>k:
                n_dict[s[left]]-=1
                left+=1
            n_max=max(n_max,right-left+1)
        return n_max
            


        