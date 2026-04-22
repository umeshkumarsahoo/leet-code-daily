class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def place(s):
            stack = []
            for char in s:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        s = place(s)
        print(s)
        t= place(t)
        print(t)
        return s==t




        