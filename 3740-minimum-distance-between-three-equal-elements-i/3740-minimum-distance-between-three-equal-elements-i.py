class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1

        min_dist = float('inf')

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j - k) + abs(i - k)
                        min_dist = min(min_dist, dist)

        return min_dist if min_dist != float('inf') else -1