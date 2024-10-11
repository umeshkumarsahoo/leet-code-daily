class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            if sum1<0:
                sum1=0
            sum1+=i
            max_sum=max(max_sum,sum1)
        return max_sum
# def solve():
#     f = open('user.out', 'w')
#     for nums in map(loads, stdin):
#         maxSum, curSum = nums[0], nums[0]
#         for num in nums[1:]:
#             if curSum < 0:
#                 curSum = num
#             else:
#                 curSum += num
#             if curSum > maxSum:
#                 maxSum = curSum
#         print(maxSum, file=f)

# solve()
# exit()
            
        


        