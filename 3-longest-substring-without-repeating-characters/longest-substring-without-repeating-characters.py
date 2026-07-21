class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":return 0
        seen=set()
        long=float('-inf')
        j=0
        for i in range(len(s)):
            while seen and  s[i] in seen :
                seen.remove(s[j])
                j+=1
            seen.add(s[i])
            long=max(len(seen),long)
        return long


        