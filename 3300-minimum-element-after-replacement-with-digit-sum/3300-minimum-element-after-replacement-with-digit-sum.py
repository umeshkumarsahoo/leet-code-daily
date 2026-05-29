class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=float('inf')
        def digit_sum(n):
            sumi=0
            while n>0:
                sumi+=n%10
                n=n//10
            return sumi
        for i in range(len(nums)):
            d=digit_sum(nums[i])
            if d<mini:
                mini=d
        return mini


                
        