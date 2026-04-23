class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack=[]
        nums1=sorted(nums)
        for i in nums1:
            stack.append(i)
        ans=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]!=stack[-1]:
                ans.append(i)
            stack.pop()
        print(ans)
        return ans[0]-ans[-1]+1 if ans else 0

        