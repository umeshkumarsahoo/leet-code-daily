class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        st_idx, ck_idx, count = 0, 0, 0
        
        while st_idx < len(g) and ck_idx < len(s):
            if g[st_idx] <= s[ck_idx]:
                st_idx += 1
                count += 1
            ck_idx += 1
            
        return count