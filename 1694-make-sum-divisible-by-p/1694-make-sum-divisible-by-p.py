class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        
        # If the total sum is already divisible by p, no need to remove any subarray
        if remainder == 0:
            return 0
        
        # Dictionary to store the remainder of prefix sums and their indices
        remainder_map = {0: -1}  # Initialize with remainder 0 at index -1
        prefix_sum = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            target_remainder = (prefix_sum - remainder) % p  # The remainder we are looking for
            
            if target_remainder in remainder_map:
                min_length = min(min_length, i - remainder_map[target_remainder])
            
            # Update the remainder_map with the current prefix_sum mod p
            remainder_map[prefix_sum] = i
        
        # If we couldn't find any valid subarray, return -1
        return min_length if min_length < len(nums) else -1
