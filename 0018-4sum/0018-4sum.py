class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def ksum(k, st, t):
            if k != 2:
                for i in range(st, len(nums) - k + 1):
                    if i > st and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    ksum(k - 1, i + 1, t - nums[i])
                    quad.pop()
                return
            l, r = st, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < t:
                    l += 1
                elif nums[l] + nums[r] > t:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        ksum(4, 0, target)
        return res