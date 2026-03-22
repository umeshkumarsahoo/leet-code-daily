class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(len(mat)):
                mat[i]=mat[i][::-1]
            return mat
        isSame=False
        for i in range(4):
            mat=rotate(mat)
            if mat==target:
                isSame=True
                break
        return isSame