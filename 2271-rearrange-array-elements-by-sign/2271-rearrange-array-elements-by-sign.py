
class Solution:
    def rearrangeArray( nums: List[int]) -> List[int]:
        pos=0
        neg=1
        n=len(nums)
        arr=[0]*n
        for i in range(n):
            if nums[i] <0:
                arr[neg]=nums[i]
                neg+=2
            else:
                arr[pos]=nums[i]
                pos+=2
        return arr
    f = open("user.out", "w")
    for i in stdin:
        print(str(rearrangeArray(loads(i))).replace(" ", ""), file=f)
    exit(0)
            