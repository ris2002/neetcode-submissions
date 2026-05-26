class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]# pair [temp,index]
        n=len(temperatures)
        res=[0]*n
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:#-1 signifies the the last pair and 0 the 1st element of that pair for ex-arr=[(1,2),(3,4),(5,6)] , arr[-1][0]=5 like matrices
                stackT,stackInd=stack.pop()
                res[stackInd]=i-stackInd
            stack.append((t,i))
        return res

        