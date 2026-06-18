class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count=0
        for i in range(k):
            if blocks[i]=='W':
                min_count+=1

        res=min_count
        for i in range(k,len(blocks)):
            if blocks[i-k]=='W':
                min_count-=1
            if blocks[i]=='W':
                min_count+=1
            res=min(res,min_count)
        return res

        
        