class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            sum_squares = 0
            while n:
                r = n % 10
                sum_squares += r * r
                n //= 10
            n = sum_squares
        return n == 1