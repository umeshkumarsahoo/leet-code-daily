class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(n):
            num=str(n)
            mul=1
            for i in num:
                mul*=int(i)
            return mul
        for i in range(n,101):
            if product(i)%t==0:
                return i
        return -1


        