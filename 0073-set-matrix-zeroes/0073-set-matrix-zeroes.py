class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[0]*len(matrix)
        col=[0]*len(matrix[0])
        for i in range(len(row)):
            for j in range(len(col)):
                if matrix[i][j]==0:
                    row[i]='*'
                    col[j]='*'
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i] =='*' or col[j] =='*':
                    matrix[i][j]=0

        return matrix

