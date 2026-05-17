class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to find the next lexicographical permutation.
        """
        g_idx = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                g_idx = i - 1
                break
        if g_idx != -1:
            swap_idx=i
            for j in range(len(nums)-1,g_idx,-1):
                if nums[j] > nums[g_idx]:
                    swap_idx=j
                    break
            nums[swap_idx], nums[g_idx] = nums[g_idx], nums[swap_idx]
        nums[g_idx + 1:] = nums[g_idx + 1:][::-1]