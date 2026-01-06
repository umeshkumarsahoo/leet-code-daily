class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        start=0
        end=n-1
        mid=0
        while mid<=end:
            if (nums[mid]==0):
                nums[mid],nums[start]=nums[start],nums[mid]
                mid+=1
                start+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                nums[end],nums[mid]=nums[mid],nums[end]
                end-=1

        

        # for i in range(n):
        #     for j in range(0,n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        
        