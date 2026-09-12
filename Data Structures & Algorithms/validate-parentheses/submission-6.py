class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')' : '(', '}' : '{', ']' : '['}
        for c in s:
            if c in valid.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != valid.get(c):
                    return False
                stack.pop()
        if stack:
            return False
        return True


            
            


        
       



            
