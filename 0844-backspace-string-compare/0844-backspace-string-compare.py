class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removeBack(s):
            stack=[]
            for i in s:
                if i=='#' and stack:
                    stack.pop()
                elif i!='#':
                    stack.append(i)
            return "".join(stack)
        s=removeBack(s)
        t=removeBack(t)
        print(s,t)
        if s=="" and t=="": return True
        return s==t
        