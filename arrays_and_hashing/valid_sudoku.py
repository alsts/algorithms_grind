import math
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell != '.':
                    if (cell in rows[r] or
                            cell in cols[c] or
                            cell in boxes[r // 3][c // 3]):
                        return False
                    else:
                        rows[r].add(cell)
                        cols[c].add(cell)
                        boxes[r // 3][c // 3].add(cell)

        return True

    def isValidSudokuDict(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell != '.':
                    if (cell in rows[r] or
                        cell in cols[c] or
                        cell in boxes[(r // 3, c // 3)]):
                        return False
                    else:
                        rows[r].add(cell)
                        cols[c].add(cell)
                        boxes[(r // 3, c // 3)].add(cell)

        return True


board = \
    [["1", "2", ".", ".", "3", ".", ".", ".", "."],
     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", ".", "3"],
     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))

board = \
    [["1", "2", ".", ".", "3", ".", ".", ".", "."],
     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "1", ".", ".", ".", ".", ".", "3"],
     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))
