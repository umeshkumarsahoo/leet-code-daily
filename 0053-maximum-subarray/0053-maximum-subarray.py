class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum,maxsum=nums[0],nums[0]
        for i in nums[1:]:
            if currsum<0:
                currsum=0
            currsum+=i
            maxsum=max(maxsum,currsum)
        return maxsum 

        