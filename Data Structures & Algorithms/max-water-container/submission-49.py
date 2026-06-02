class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=-1
        for i in range(len(heights)):
            min_num=h_num=None
            j=0
            while j<len(heights)-1:
                
                if j==i:
                    j+=1
                    continue
                elif i<j:
                    h_num=j-i
                elif i>j:
                    h_num=i-j
                if heights[i]<heights[j]:
                    min_num=heights[i]
                else:
                    min_num=heights[j]
                area=h_num*min_num
                j+=1
                max_area=max(max_area,area)
        return max_area
                
            

                



        