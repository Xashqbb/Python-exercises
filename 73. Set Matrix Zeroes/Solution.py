class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        zero_rows = set()
        zero_columns = set()

        # Find rows and columns with zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)

        # Zero out rows and columns
        for i in zero_rows:
            for j in range(n):
                matrix[i][j] = 0

        for j in zero_columns:
            for i in range(m):
                matrix[i][j] = 0
        return matrix