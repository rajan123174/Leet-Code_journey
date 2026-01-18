class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]

        # Check if k x k magic square starting at (r, c)
        def is_magic(r, c, k):
            target = row[r][c + k] - row[r][c]

            # Rows
            for i in range(r, r + k):
                if row[i][c + k] - row[i][c] != target:
                    return False

            # Columns
            for j in range(c, c + k):
                if col[r + k][j] - col[r][j] != target:
                    return False

            # Diagonals
            d1 = d2 = 0
            for i in range(k):
                d1 += grid[r + i][c + i]
                d2 += grid[r + i][c + k - 1 - i]

            return d1 == target and d2 == target

        # Try largest k first
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k

        return 1
