class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        k=len(needle)
        if k==len(haystack): return 0 if haystack==needle else -1
        while i<=len(haystack)-k:
            if haystack[i:i+k]==needle: return i
            i+=1
        return -1 

