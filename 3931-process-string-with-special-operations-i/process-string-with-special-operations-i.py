class Solution:
    def processStr(self, s: str) -> str:
        str1=[]
        s_list=list(s)
        for char in s_list:
            if char == '*':
                if str1:
                    str1.pop()
            elif char == '#':
                str2 = str1[::]
                for x in str2:
                    str1.append(x)
            elif char == '%':
                str1 = str1[::-1]
            else:
                str1.append(char)
        return "".join(str1)