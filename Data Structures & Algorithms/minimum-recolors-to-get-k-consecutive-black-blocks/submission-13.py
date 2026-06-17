class Solution:
    def dict_n(self,string:str,alpha:str):
        n_dict={}
        for char in string:
            n_dict[char]=n_dict.get(char, 0) + 1
        return n_dict.get(alpha, 0)
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        right=k
       
        min_ctr=100000001
        while(right<len(blocks)+1):
            ctr=self.dict_n(blocks[left:right],'W')
            min_ctr=min(min_ctr,ctr)
            left+=1
            right+=1
        return min_ctr

          

