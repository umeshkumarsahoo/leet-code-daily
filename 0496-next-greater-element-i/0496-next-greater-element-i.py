class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        for i in range(len(nums1)):
            idx=nums2.index(nums1[i])
            for j in range(idx,len(nums2)):
                if nums2[j]>nums1[i]:
                    nums1[i]=nums2[j]
                    break
            else:
                nums1[i]=-1
        return nums1