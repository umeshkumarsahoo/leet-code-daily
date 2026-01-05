class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        mino,maxo=-1,-1
        n=len(nums)
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                mino=mid
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
                maxo=mid
                start=mid+1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if mino and  maxo==-1 :
            maxo=mino
        elif mino==-1 and  maxo:
            mino=maxo
        return [mino,maxo]

        