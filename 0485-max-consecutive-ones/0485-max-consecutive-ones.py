class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        curr=0
        for i in nums:
            if i==1:
                curr+=1
                maxi=max(curr,maxi)
            else: curr=0
        return maxi

            

        