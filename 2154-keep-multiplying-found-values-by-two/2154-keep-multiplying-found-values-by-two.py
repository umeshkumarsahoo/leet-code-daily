class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d=set(nums)
        while original in d:
            original*=2
        return original

        