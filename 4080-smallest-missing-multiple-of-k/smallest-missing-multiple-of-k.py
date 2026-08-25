class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set=set()
        for num in nums:
            num_set.add(num)
        for i in range(1,101):
            if k*i not in num_set:
                return k*i
        return k*101