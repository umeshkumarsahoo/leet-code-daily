class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            near, far = i + 1, len(nums) - 1
            while near < far:
                total = nums[i] + nums[near] + nums[far]
                if total == 0:
                    res.append([nums[i], nums[near], nums[far]])
                    while near < far and nums[near] == nums[near + 1]:
                        near += 1
                    while near < far and nums[far] == nums[far - 1]:
                        far -= 1
                    near += 1
                    far -= 1
                elif total < 0:
                    near += 1
                else:
                    far -= 1
        return res