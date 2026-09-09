class Solution:
    def solveNQueens(self, n):
        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diag = set()
        neg_diag = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if (
                    col in cols
                    or row + col in pos_diag
                    or row - col in neg_diag
                ):
                    continue

                board[row][col] = "Q"

                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."

                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        backtrack(0)

        return result