"""
You are given a 9 x 9 Sudoku board. A Sudoku board is valid if the following rules are followed:
  1. Each row must contain the digits 1-9 without duplicates.
  2. Each column must contain the digits 1-9 without duplicates.
  3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false.
Note: A board does not need to be full or be solvable to be valid.

Constraints:
  board.length == 9
  board[i].length == 9
  board[i][j] is a digit 1-9 or '.'

Time Complexity: O(1), Memory Complexity: O(1)
  board is always 9x9 → 81 cells, 27 sets. For an n x n board: O(n²) time and memory.

Notes:
  - Skip '.' first, otherwise the 2nd empty cell looks like a duplicate.
  - Box id = (r // 3, c // 3) → 0..2 each, tuple works as dict key.
  - Lists instead of defaultdict work the same (see inline comments), slightly faster (no hashing).
"""

from collections import defaultdict
from typing import List

import pytest


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # [set() for _ in range(9)]
        cols = defaultdict(set) # [set() for _ in range(9)]
        boxes = defaultdict(set) # [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell == ".":
                   continue

                if (cell in rows[r] or
                   cell in cols[c] or
                   cell in boxes[(r // 3, c // 3)]):
                       return False
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[(r // 3, c // 3)].add(cell) # boxes[r // 3][c // 3].add(cell) for boxes list

        return True


# Add each new variant's method name here.
METHODS = ["isValidSudoku"]

EXAMPLE_1 = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

EXAMPLE_2 = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def empty_board():
    return [["."] * 9 for _ in range(9)]


def board_with(*cells):
    """cells: (row, col, digit)"""
    board = empty_board()
    for r, c, d in cells:
        board[r][c] = d
    return board


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "board, expected",
    [
        pytest.param(EXAMPLE_1, True, id="example_1"),
        pytest.param(EXAMPLE_2, False, id="example_2_box_duplicate"),
        pytest.param(empty_board(), True, id="empty_board"),
        pytest.param(board_with((0, 0, "5"), (0, 8, "5")), False, id="row_duplicate"),
        pytest.param(board_with((0, 4, "7"), (8, 4, "7")), False, id="column_duplicate"),
        pytest.param(board_with((3, 3, "2"), (5, 5, "2")), False, id="box_duplicate_middle_box"),
        pytest.param(board_with((6, 8, "9"), (8, 6, "9")), False, id="box_duplicate_last_box"),
        pytest.param(board_with((0, 0, "3"), (1, 3, "3"), (2, 6, "3")), True, id="same_digit_diff_rows_cols_boxes"),
        pytest.param(board_with((0, 2, "4"), (0, 3, "5")), True, id="neighbours_across_box_border"),
        pytest.param(board_with((2, 2, "6"), (3, 3, "6")), True, id="diagonal_neighbours_diff_boxes"),
    ],
)
def test_is_valid_sudoku(method, board, expected):
    assert getattr(Solution(), method)(board) == expected
