class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        strict_inc=1
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=1
            else:
                strict_inc=max(count,strict_inc)
                count=1
        strict_inc=max(count,strict_inc)
        strict_dec=1
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
            else:
                strict_dec=max(count,strict_dec)
                count=1
        strict_dec=max(count,strict_dec)
        return max(strict_dec,strict_inc)