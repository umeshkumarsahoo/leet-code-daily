class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        i=x
        j=x+k-1
        max_col=y+k
        while i<j:
            for k in range(y,max_col):
                temp=grid[i][k]
                grid[i][k]=grid[j][k]
                grid[j][k]=temp
            i+=1
            j-=1
        return grid


            