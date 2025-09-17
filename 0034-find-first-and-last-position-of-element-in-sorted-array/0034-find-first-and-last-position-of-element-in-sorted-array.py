class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mini,maxi=-1,-1
        n=len(nums)
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                mini=mid
                end=mid-1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                maxi=mid
                start=mid+1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if mini and  maxi==-1 :
            maxi=mini
        elif mini==-1 and  maxi:
            mini=maxi
        return [mini,maxi] 
