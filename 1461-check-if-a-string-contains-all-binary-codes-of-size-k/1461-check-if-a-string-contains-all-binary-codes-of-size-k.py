class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        strings=set()
        codes=2**k
        for i in range(k,len(s)+1):
            sub_str=s[i-k:i]
            if sub_str not in strings:
                strings.add(sub_str)
                codes-=1
            if codes==0: return True
        return False