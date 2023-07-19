class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        # Create empty rows to store characters
        rows = [''] * numRows
        # Current row and direction variables
        curr_row = 0
        direction = -1
        # Iterate through the string
        for char in s:
            rows[curr_row] += char
            # Change direction if at the top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1
            # Move to the next row based on the direction
            curr_row += direction
        # Join all rows together
        return ''.join(rows)