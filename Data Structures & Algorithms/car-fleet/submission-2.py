class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[(p,s) for p,s in zip(position,speed)]
        cars.sort(reverse=True)#ordering is important in stack problems
        stack=[]
        for p,s in cars:
            t=(target-p)/s
            stack.append(t)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        