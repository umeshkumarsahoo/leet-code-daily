class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0
        sign=1
        while i<n and (s[i]==' '): i+=1
        if i==n: return 0
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            sign=1
            i+=1
        INT_MAX=2**31-1
        INT_MIN=-2**31
        res=0
        while i < n and s[i].isdigit():
            digit=int(s[i])
            res=res*10+digit
            if sign*res<=INT_MIN:
                return INT_MIN
            if sign*res>=INT_MAX:
                return INT_MAX
            i+=1
        return res*sign 
