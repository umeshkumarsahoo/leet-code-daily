class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        flat=[x for lst in nums for x in lst]
        counts=Counter(flat)
        items=counts.items()
        res=[key for (key,value) in items if value ==len(nums)]
        return sorted(res) 
        