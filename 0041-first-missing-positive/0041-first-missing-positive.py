class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        nums=sorted(nums)
        missing_no = 1
        for n in nums:
            if n == missing_no:
                missing_no += 1
            elif n > missing_no:
                return missing_no
        return missing_no
        
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().firstMissingPositive(nums),file=f)
exit(0)