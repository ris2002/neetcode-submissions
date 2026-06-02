class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_area=0
        min_height=1001

        while(i<j):
            height=min(heights[i],heights[j])
            
            
            width=j-i
            area=width*height
            max_area=max(area,max_area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return max_area

                
           
           


        




           
            
            
           
        return max_area
