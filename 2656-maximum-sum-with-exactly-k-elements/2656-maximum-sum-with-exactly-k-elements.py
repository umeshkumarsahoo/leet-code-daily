class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_sum = 0
        for _ in range(k):
            curr_sum += nums[-1]
            nums[-1] += 1
        return curr_sum
                
            