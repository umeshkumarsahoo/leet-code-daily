class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            near,far=i+1,len(nums)-1
            while near<far:
                if nums[near]+nums[far]+nums[i]==0:
                    res.append([nums[near],nums[far],nums[i]])
                    while near<far and nums[near]==nums[near+1]:
                        near+=1
                    while near<far and nums[far]==nums[far-1]:
                        far-=1
                    near+=1
                    far-=1
                elif nums[near]+nums[far]+nums[i]>0:
                    far-=1
                else:
                    near+=1
        return res


        