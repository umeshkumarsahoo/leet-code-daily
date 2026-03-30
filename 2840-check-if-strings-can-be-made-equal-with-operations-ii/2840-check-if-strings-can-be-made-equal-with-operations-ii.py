class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return 'false'
        # even1=sorted(list(s1[0::2]))
        # even2=sorted(list(s2[0::2]))
        # odd1=sorted(list(s1[1::2]))
        # odd2=sorted(list(s2[1::2]))
        # return even1==even2 and odd1==odd2
        return Counter(s1[::2])==Counter(s2[::2]) and Counter(s1[1::2])==Counter(s2[1::2])
        