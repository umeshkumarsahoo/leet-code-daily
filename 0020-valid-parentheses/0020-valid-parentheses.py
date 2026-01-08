class Solution:
    def isValid(self, s: str) -> bool:
        par =list(s)
        stack=[]
        isPar=True
        if len(par)==1:
            return False
        for i in par:
            if i=='(' or i== '[' or i=='{':
                stack.append(i)
            elif len(stack)==0:
                return False
            elif i==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif i==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif i=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        if len(stack)!=0:
            return False
        return isPar