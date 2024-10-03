class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0
        remainder_map = {0: -1} 
        prefix_sum = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            target_remainder = (prefix_sum - remainder) % p 
            if target_remainder in remainder_map:
                min_length = min(min_length, i - remainder_map[target_remainder])
            remainder_map[prefix_sum] = i
        return min_length if min_length < len(nums) else -1
