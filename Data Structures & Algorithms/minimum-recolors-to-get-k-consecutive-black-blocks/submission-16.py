class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_s=0
        for i in range(k):
            if blocks[i]=='W':
                min_s+=1
        
        res=min_s
        for i in range(k,len(blocks)):
            if blocks[i-k]=='W':
                min_s-=1
            if blocks[i]=='W':
                min_s+=1
            res=min(res,min_s)
        return res

        