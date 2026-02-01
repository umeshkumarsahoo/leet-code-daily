class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sumi=nums[0]
        num=sorted(nums[1:])[::-1]
        print(num)
        for i in range(2):
            sumi+=num.pop()
        return sumi

