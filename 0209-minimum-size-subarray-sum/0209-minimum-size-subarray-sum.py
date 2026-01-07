class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        else:
            min_len_window=float('inf')
            subarr_sum=0
            r,l=0,0
            while r <len(nums):
                subarr_sum+=nums[r]
                r+=1
                while subarr_sum>=target:
                    curr_window=r-l
                    min_len_window=min(min_len_window,curr_window)
                    subarr_sum-=nums[l]
                    l+=1
            return min_len_window
                
                
