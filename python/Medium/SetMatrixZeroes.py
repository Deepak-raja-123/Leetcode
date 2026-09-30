class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check first row
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_zero = True

        # Check first column
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_zero = True

        # Use first row and first column as markers
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Set marked rows to zero
        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(1, cols):
                    matrix[row][col] = 0

        # Set marked columns to zero
        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0

        # Handle first row
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0

        # Handle first column
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0