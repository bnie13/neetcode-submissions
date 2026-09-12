class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')' : '(', '}' : '{', ']' : '['}
        for c in s:
            if c not in valid:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != valid.get(c):
                    return False
                stack.pop()
        return not stack


            
            


        
       



            
