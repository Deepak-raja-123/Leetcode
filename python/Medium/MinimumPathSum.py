class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):

                if row == 0 and col == 0:
                    continue

                if row == 0:
                    grid[row][col] += grid[row][col - 1]

                elif col == 0:
                    grid[row][col] += grid[row - 1][col]

                else:
                    grid[row][col] += min(
                        grid[row - 1][col],
                        grid[row][col - 1]
                    )

        return grid[rows - 1][cols - 1]