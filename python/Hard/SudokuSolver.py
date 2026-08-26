class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def backtrack():
            # Find the empty cell with the fewest possibilities
            best_row = -1
            best_col = -1
            best_options = None

            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        box = (r // 3) * 3 + (c // 3)

                        options = []

                        for num in "123456789":
                            if (num not in rows[r] and
                                num not in cols[c] and
                                num not in boxes[box]):
                                options.append(num)

                        if not options:
                            return False

                        if best_options is None or len(options) < len(best_options):
                            best_row = r
                            best_col = c
                            best_options = options

            # No empty cells → solved
            if best_options is None:
                return True

            box = (best_row // 3) * 3 + (best_col // 3)

            for num in best_options:

                board[best_row][best_col] = num
                rows[best_row].add(num)
                cols[best_col].add(num)
                boxes[box].add(num)

                if backtrack():
                    return True

                # Undo
                board[best_row][best_col] = '.'
                rows[best_row].remove(num)
                cols[best_col].remove(num)
                boxes[box].remove(num)

            return False

        backtrack()