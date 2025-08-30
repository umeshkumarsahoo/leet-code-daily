class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        n=len(nums)
        for i in nums:
            count[i]=count.get(i,0)+1
        for key,item in count.items():
            if item>(n//2):
                return key
        return None


        