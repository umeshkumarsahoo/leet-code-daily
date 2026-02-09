class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # def mul(i):
        #     m=1
        #     for j in range(i):
        #         m*=nums[j]
        #     for j in range(len(nums)-1,i,-1):
        #         m*=nums[j]
        #     return m
        res=[0]*len(nums)
        pre=1
        res[0]=pre
        for i in range(1,len(nums)):
            res[i]=pre*nums[i-1]
            pre*=nums[i-1]
        print(res)
        post=1
        for i in range(len(nums)-1,0,-1):
            post*=nums[i]
            res[i-1]*=post
        return res



        