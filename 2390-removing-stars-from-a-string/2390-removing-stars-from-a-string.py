class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if not stack and s[i]=='*': continue
            elif stack and s[i]=='*':
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)

        