class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1

        for row in obstacleGrid:
            for col in range(n):
                if row[col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] = dp[col] + dp[col - 1]

        return dp[n - 1]