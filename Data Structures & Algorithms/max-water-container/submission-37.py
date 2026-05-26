class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        for i in range(len(heights)):
            
            for j in range(i+1,len(heights)):
                x=min(heights[i],heights[j])
                area=x*(j-i)
                print('x:',x)
                print('j-1:',j-i)
                print('area:',area)
                max_area=max(max_area,area)
        return max_area
        
        