class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return a[:i]
        pref = strs[0]
        for i in range(1, len(strs)):
            pref = prefix(pref, strs[i])
        return pref