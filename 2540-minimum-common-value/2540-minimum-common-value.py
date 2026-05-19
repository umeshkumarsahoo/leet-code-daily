class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num=set()
        for n in nums1: num.add(n)
        for n in nums2: 
            if n in num: return n
        return -1
        