class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:return -1
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        mins=0
        directions=[(0,1),(0,-1),(-1,0),(1,0)]
        while q:
            for _ in range(len(q)):   
                r,c=q.popleft()
                for (i,j) in directions:
                    nr=r+i
                    nc=c+j
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and fresh:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            mins+=1
        return mins-1 if not fresh else -1






            