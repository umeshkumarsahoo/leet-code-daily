class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        k=n//3
        freq=defaultdict()
        for i in nums:
            freq[i]=freq.get(i,0)+1
        res=[]
        for key,value in freq.items():
            if value>k: res.append(key)  
        return res      