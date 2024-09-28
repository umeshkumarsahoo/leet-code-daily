class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return nums[i]
        # return -1
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return nums[i]
        return -1
        


        