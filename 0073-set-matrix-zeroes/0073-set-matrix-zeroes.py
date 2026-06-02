class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=set()
        col=set()
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        for i in row:
            matrix[i]=[0]*cols
        for j in col:
            for i in range(rows):
                matrix[i][j]=0
        return matrix
                

        