class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        for  i  in range(n):
            step=nums[i]
            if step==0:
                continue
            j=(i+step)%n
            if j<0:
                j+=n
            res[i]=nums[j]
        return res