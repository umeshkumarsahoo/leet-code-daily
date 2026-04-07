class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid > 0 and mid < len(nums) - 1:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] < nums[mid + 1]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    return mid + 1
            else:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    return mid - 1
        return start
