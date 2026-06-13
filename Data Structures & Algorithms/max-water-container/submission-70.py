class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        max_area=0
        j=len(heights)-1
        while(i<j):
            if heights[i]<heights[j]:
                x=heights[i]
                width=j-i
                i+=1
            elif heights[i]>heights[j]:
                x=heights[j]
                width=j-i
                j-=1
            elif heights[i]==heights[j]:
                x=heights[j]
                width=j-i
                i+=1
                j-=1


            
            
            prod=x*width
            max_area=max(max_area,prod)
        return max_area
            
        