from math import ceil
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        time=ceil(len(b)/len(a))
        temp=time*a
        if b in temp: return time
        if b in temp+a: return time+1
        return -1
        