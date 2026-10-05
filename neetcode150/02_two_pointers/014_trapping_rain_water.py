"""
You are given an array of non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
Water above bar i = min(max height on the left, max height on the right) - height[i], if positive.

Constraints:
  1 <= height.length <= 1000
  0 <= height[i] <= 1000

trapBrute   Time: O(n²)  Memory: O(1)
trapPrefix  Time: O(n)   Memory: O(n)
trap        Time: O(n)   Memory: O(1)

Notes:
  - Count one column at a time: water[i] = min(tallest left, tallest right) - height[i].
  - Subtract height[i]: the bar is ground, water sits on top of it.
  - Prefix: maxL[] left → right, maxR[] right → left (like Product Except Self, with max).
    Inclusive: maxL[i] = max(maxL[i - 1], height[i]), edges = height[0] / height[-1] (not 0, or outer walls are lost).
    Includes the bar itself → water never negative.
  - Two pointers: settle the side with the LOWER max → its level is known, the other side is at least as tall.
  - Update max BEFORE adding water → a new tallest bar adds 0, never negative.
  - Short bumps below the level get covered; a taller bump becomes the new wall for columns past it.
"""

from typing import List

import pytest


class Solution:
    def trapBrute(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        n = len(height)

        # one column of water per bar
        for i in range(n):
            left_max = right_max = height[i]  # start at bar itself → never negative

            for j in range(0, i):  # tallest wall on the left
                left_max = max(left_max, height[j])
            for j in range(i + 1, n):  # tallest wall on the right
                right_max = max(right_max, height[j])

            res += min(left_max, right_max) - height[i]  # lower wall = water level, minus ground

        return res

    def trapPrefix(self, height: List[int]) -> int:
        if not height:
            return 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[len(height) - 1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(len(height)):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                res += water

        return res

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        while l < r:
            if left_max < right_max:  # lower wall decides the level → settle left
                l += 1
                left_max = max(left_max, height[l])  # tallest so far vs new bar
                res += left_max - height[l]  # lower than wall → water; new wall → 0
            else:  # right wall is lower (or equal) → settle right
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res


# Add each new variant's method name here.
METHODS = ["trapBrute", "trap", "trapPrefix"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "height, expected",
    [
        pytest.param([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9, id="example_1"),
        pytest.param([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, id="leetcode_example_1"),
        pytest.param([4, 2, 0, 3, 2, 5], 9, id="leetcode_example_2"),
        pytest.param([5], 0, id="single_bar"),
        pytest.param([3, 3], 0, id="two_bars"),
        pytest.param([0, 0, 0], 0, id="flat_ground"),
        pytest.param([1, 2, 3, 4], 0, id="increasing_no_left_wall"),
        pytest.param([4, 3, 2, 1], 0, id="decreasing_no_right_wall"),
        pytest.param([3, 0, 3], 3, id="simple_bowl"),
        pytest.param([5, 0, 1], 1, id="limited_by_shorter_wall"),
        pytest.param([2, 0, 2, 0, 2], 4, id="two_pools"),
        pytest.param([5, 1, 2, 1, 5], 11, id="bumpy_floor"),
    ],
)
def test_trap(method, height, expected):
    assert getattr(Solution(), method)(height) == expected
