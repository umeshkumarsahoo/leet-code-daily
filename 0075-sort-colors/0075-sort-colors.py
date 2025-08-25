class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        idx=0
        for i in range(3):
            freq=count.get(i,0)
            nums[idx:idx+freq]=[i]*freq
            idx+=freq
                
            
                