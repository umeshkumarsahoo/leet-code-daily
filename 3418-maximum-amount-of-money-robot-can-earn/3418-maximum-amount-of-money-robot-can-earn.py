class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        dp = [[[None]*3 for _ in range(n)] for _ in range(m)]
        
        def solve(i, j, skip):
            if i >= m or j >= n:
                return float('-inf')
            
            if dp[i][j][skip] is not None:
                return dp[i][j][skip]
            
            # Base case
            if i == m-1 and j == n-1:
                if coins[i][j] < 0 and skip > 0:
                    return 0
                return coins[i][j]
            
            # Normal move
            down = solve(i+1, j, skip)
            right = solve(i, j+1, skip)
            
            normal = max(down, right) + coins[i][j]
            
            # Skip negative coin
            skip_option = float('-inf')
            if coins[i][j] < 0 and skip > 0:
                down_skip = solve(i+1, j, skip-1)
                right_skip = solve(i, j+1, skip-1)
                skip_option = max(down_skip, right_skip)
            
            dp[i][j][skip] = max(normal, skip_option)
            return dp[i][j][skip]
        
        return solve(0, 0, 2)


        