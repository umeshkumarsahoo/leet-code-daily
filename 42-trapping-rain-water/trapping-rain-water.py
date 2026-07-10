class Solution:
    def trap(self, height: List[int]) -> int:
        l_max=[]
        r_max=[]
        n=len(height)
        for i in range(n):
            if l_max:
                maxi=max(l_max[-1],height[i])
            else:
                maxi=height[i]
            l_max.append(maxi)
        for i in range(n-1,-1,-1):
            if r_max:
                maxi=max(r_max[-1],height[i])
            else:
                maxi=height[i]
            r_max.append(maxi)
        r_max=r_max[::-1]
        ans=0
        for i in range(n):
            mini=min(l_max[i],r_max[i])
            ans+=(mini-height[i])
        return ans

        