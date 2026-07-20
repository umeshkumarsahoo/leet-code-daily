class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=['.'*n  for _ in range(n)]
        def Valid(row,col):
            for i in range(row):
                pos=board[i].index('Q')
                if pos==col or abs(col-pos)==abs(row-i): return False
            return True
        def dfs(row):
            if row==n: 
                res.append(board[:])
                return 
            for c in range(n):
                if Valid (row,c):
                    board[row]='.'*c+'Q'+"."*(n-c-1)
                    dfs(row+1)
                    board[row]='.'*n
        dfs(0)
        return res
        