class Solution:
        def areSimilar(self, mat: List[List[int]], k: int) -> bool:
            k %= len(mat[0])
            original_mat = [row[:] for row in mat]

            def shift_row(row, shift, direction):
                n = len(row)
                shifted_row = [0] * n
                for i in range(n):
                    if direction == "left":
                        shifted_row[(i + (n - shift)) % n] = row[i]
                    else:
                        shifted_row[(i + shift) % n] = row[i]
                return shifted_row

            for i in range(len(mat)):
                if i % 2 == 0:
                    mat[i] = shift_row(mat[i], k, "left")
                else:
                    mat[i] = shift_row(mat[i], k, "right")

            return mat == original_mat
 


            