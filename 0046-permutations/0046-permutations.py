class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        def backtrack(start):
            if start==len(nums):
                res.append(nums.copy())
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                backtrack(start+1)
                nums[start],nums[i]=nums[i],nums[start]
        backtrack(0)
        return res