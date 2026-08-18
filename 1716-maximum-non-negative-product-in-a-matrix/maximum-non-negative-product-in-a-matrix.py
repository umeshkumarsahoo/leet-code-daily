
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_dp = [[0] * m for _ in range(n)]
        min_dp = [[0] * m for _ in range(n)]

        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        for i in range(1, n):
            max_dp[i][0] = max_dp[i-1][0] * grid[i][0]
            min_dp[i][0] = min_dp[i-1][0] * grid[i][0]

        for j in range(1, m):
            max_dp[0][j] = max_dp[0][j-1] * grid[0][j]
            min_dp[0][j] = min_dp[0][j-1] * grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                max_dp[i][j] = max(max_dp[i-1][j] * grid[i][j], max_dp[i][j-1] * grid[i][j], min_dp[i-1][j] * grid[i][j], min_dp[i][j-1] * grid[i][j])
                min_dp[i][j] = min(max_dp[i-1][j] * grid[i][j], max_dp[i][j-1] * grid[i][j], min_dp[i-1][j] * grid[i][j], min_dp[i][j-1] * grid[i][j])

        if max_dp[n-1][m-1] >= 0:
            return max_dp[n-1][m-1] % (10**9 + 7)
        else:
            return -1