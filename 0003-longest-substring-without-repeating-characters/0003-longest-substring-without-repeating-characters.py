class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        seen=set()
        maxi=float('-inf')
        j=0
        for i in range(len(s)):
            while seen and s[i] in seen:
                seen.remove(s[j])
                j+=1
            seen.add(s[i])
            maxi=max(len(seen),maxi)
        return maxi
        