class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        dist=float('inf')
        for i,n in enumerate(nums):
            if n==target:
                dist=min(abs(i-start),dist)

        return dist
        