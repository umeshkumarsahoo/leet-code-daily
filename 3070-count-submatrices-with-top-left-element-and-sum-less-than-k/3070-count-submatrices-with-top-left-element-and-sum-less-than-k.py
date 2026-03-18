class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row=len(grid)
        col=len(grid[0])
        count=0
        for i in range(row):
            for j in range(col):
                if i-1>=0:grid[i][j]+=grid[i-1][j]
                if j-1>=0:grid[i][j]+=grid[i][j-1]
                if i-1>=0 and j-1>=0: grid[i][j]-=grid[i-1][j-1]
                if grid[i][j]<=k:
                    count+=1
                else:
                    break
        return count

        