class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {num: i for i, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        for i, num in enumerate(nums2):
            if num in index_map:
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > num:
                        result[index_map[num]] = nums2[j]
                        break
        return result