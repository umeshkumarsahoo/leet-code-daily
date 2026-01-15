class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for char in s:
            if char=='(':
                stack.append(char)
            else:
                if stack and char==')':
                    stack.pop()
                elif not stack and char :
                    count+=1
        return len(stack)+count 

                

        