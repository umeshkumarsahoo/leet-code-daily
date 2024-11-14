class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique = set()
        result = []
        for i in nums:
            if not i in unique:
                unique.add(i)
                continue
            result.append(i)  
        return result