class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countmap={}
        for i,num in enumerate(nums):
            comp=target-num
            if comp in countmap:
                return [countmap[comp],i]
            countmap[num]=i
        return []