class Solution:
    '''In Python, pop() does two things at once:

Removes the last element from the list (the “top” of the stack)

Returns that element so you can assign it to a variable or use it in an expression'''
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        
        for c in tokens:
            
            if c=='+':
                right=stack.pop() #Last in First out 
                left=stack.pop()
                stack.append(left+right)
            elif c=='-':
                right=stack.pop() #Last in First out 
                left=stack.pop()
                stack.append(left-right)
            elif c=='*':
                right=stack.pop() #Last in First out 
                left=stack.pop()
                stack.append(left*right)
            elif c=='/':
                right=stack.pop() #Last in First out 
                left=stack.pop()
                stack.append(int(float(left) / right))
            else:
                stack.append(int(c))
        return stack[0]
        