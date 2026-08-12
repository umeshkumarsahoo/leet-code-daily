class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0
        freq=defaultdict()
        j=0
        for i in range(n):
            freq[nums[i]]=1+freq.get(nums[i],0)
            while freq[nums[i]]>k:
                freq[nums[j]]-=1
                j+=1
            max_len=max(max_len,i-j+1)
        return max_len