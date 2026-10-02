"""
You are given an array of non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
Water above bar i = min(max height on the left, max height on the right) - height[i], if positive.

Constraints:
  1 <= height.length <= 1000
  0 <= height[i] <= 1000

Time Complexity: __, Memory Complexity: __
"""

from typing import List

import pytest


class Solution:
    def trap(self, height: List[int]) -> int:
        return 0


# Add each new variant's method name here.
METHODS = ["trap"]


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
