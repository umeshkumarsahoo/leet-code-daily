class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem={}

        for i,num in enumerate(nums):
            comp=target-num
            if comp in rem:
                return [rem[comp],i]
            rem[num]=i
        return []