class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        size=float('inf')
        sumi=0
        for i in range(len(nums)):
                sumi+=nums[i]
                while sumi>=target:
                    size=min(i-j+1,size)
                    sumi-=nums[j]
                    j+=1
        return size if size!=float('inf') else 0
