import math
class Solution:
    def requiredTime(self,k,piles):
        t_time=0
        for pile in piles:
            t_time+=math.ceil(pile/k)
        return t_time
    def minEatingSpeed(self, piles, h):
        start=1
        end=max(piles)
        ans=end
        while start<=end:
            mid=(start+end)//2
            if self.requiredTime(mid,piles)<=h:
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans