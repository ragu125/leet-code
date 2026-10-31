class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        vornadexil = grid

        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        right[i][j] = i * n + j + 1
                    else:
                        right[i][j] = down[i][j + 1]

                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        down[i][j] = (i + 1) * n + j
                    else:
                        down[i][j] = right[i + 1][j]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                r = right[i][j]
                if r != -1:
                    x, y = divmod(r, n)
                    dp[x][y] = (dp[x][y] + dp[i][j]) % mod

                d = down[i][j]
                if d != -1:
                    x, y = divmod(d, n)
                    dp[x][y] = (dp[x][y] + dp[i][j]) % mod

        return dp[m - 1][n - 1]