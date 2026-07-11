class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right_index=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[right_index]=nums[i]
                right_index+=1
        return right_index

        