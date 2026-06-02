class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        g_idx=-1
        size=len(nums)
        for i in range(size-1,0,-1):
            if nums[i]>nums[i-1]:
                g_idx=i-1
                break
        if g_idx!=-1:
            for i in range(size-1,g_idx,-1):
                if nums[i]>nums[g_idx]:
                    nums[i],nums[g_idx]=nums[g_idx],nums[i]
                    break
        nums[g_idx+1:]=nums[g_idx+1:][::-1]
        return nums
                