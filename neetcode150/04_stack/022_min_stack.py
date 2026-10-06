"""
Design a stack class that supports the push, pop, top, and getMin operations.

  MinStack()        initializes the stack object.
  push(val)         pushes the element val onto the stack.
  pop()             removes the element on the top of the stack.
  top()             gets the top element of the stack.
  getMin()          retrieves the minimum element in the stack.

Each function should run in O(1) time.

Constraints:
  -2^31 <= val <= 2^31 - 1
  pop, top and getMin will always be called on non-empty stacks.

Time Complexity: __, Memory Complexity: __
"""

from typing import List

import pytest


class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        return 0

    def getMin(self) -> int:
        return 0


# Add each new variant's class name here.
CLASSES = ["MinStack"]


# LeetCode style: ops[i] is called with args[i]; expected[i] is its return value (None for push/pop).
@pytest.mark.parametrize("cls", CLASSES)
@pytest.mark.parametrize(
    "ops, args, expected",
    [
        pytest.param(
            ["push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[1], [2], [0], [], [], [], []],
            [None, None, None, 0, None, 2, 1],
            id="example_1",
        ),
        pytest.param(
            ["push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[-2], [0], [-3], [], [], [], []],
            [None, None, None, -3, None, 0, -2],
            id="leetcode_example",
        ),
        pytest.param(
            ["push", "top", "getMin"],
            [[5], [], []],
            [None, 5, 5],
            id="single_element",
        ),
        pytest.param(
            ["push", "push", "getMin", "pop", "getMin"],
            [[2], [2], [], [], []],
            [None, None, 2, None, 2],
            id="duplicate_min_survives_pop",
        ),
        pytest.param(
            ["push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
            [[3], [2], [1], [], [], [], [], []],
            [None, None, None, 1, None, 2, None, 3],
            id="min_restored_after_each_pop",
        ),
        pytest.param(
            ["push", "push", "push", "getMin", "top"],
            [[1], [2], [3], [], []],
            [None, None, None, 1, 3],
            id="min_stays_at_bottom",
        ),
        pytest.param(
            ["push", "pop", "push", "getMin", "top"],
            [[1], [], [7], [], []],
            [None, None, None, 7, 7],
            id="empty_then_reused",
        ),
        pytest.param(
            ["push", "push", "getMin", "top"],
            [[-(2**31)], [2**31 - 1], [], []],
            [None, None, -(2**31), 2**31 - 1],
            id="extreme_values",
        ),
    ],
)
def test_min_stack(cls, ops, args, expected):
    stack = globals()[cls]()
    results = [getattr(stack, op)(*arg) for op, arg in zip(ops, args)]
    assert results == expected
