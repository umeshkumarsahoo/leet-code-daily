class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(0,len(nums)):
            if i not in nums:
                return i
        return nums[-1]+1   
        