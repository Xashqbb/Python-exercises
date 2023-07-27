class Solution(object):
    def rotate(self, matrix):

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                # Save the top left element
                topLeft = matrix[l][l + i]

                # Move bottom left into top left
                matrix[l][l + i] = matrix[r - i][l]

                # Move bottom right into bottom left
                matrix[r - i][l] = matrix[r][r - i]

                # Move top right into bottom right
                matrix[r][r - i] = matrix[l + i][r]

                # Move top left into top right
                matrix[l + i][r] = topLeft

            r -= 1
            l += 1
