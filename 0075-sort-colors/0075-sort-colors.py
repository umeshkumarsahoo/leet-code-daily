class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums
        