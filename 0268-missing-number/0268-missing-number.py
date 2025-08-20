class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        mis_num = 0
        for num in nums:
            if num == mis_num:
                mis_num += 1
            else:
                return mis_num
        return mis_num