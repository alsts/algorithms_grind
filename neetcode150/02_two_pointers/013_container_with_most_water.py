"""
You are given an integer array heights where heights[i] represents the height of the i-th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
Water held = min(heights[l], heights[r]) * (r - l).

Constraints:
  2 <= heights.length <= 1000
  0 <= heights[i] <= 1000

Time Complexity: O(n), Memory Complexity:O(1)
"""

from typing import List

import pytest


class Solution:
    def maxAreaBrute(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            width = r - l
            min_bar_height = min(heights[l], heights[r])
            max_area = max(max_area, min_bar_height * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


# Add each new variant's method name here.
METHODS = ["maxArea"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "heights, expected",
    [
        pytest.param([1, 7, 2, 5, 4, 7, 3, 6], 36, id="example_1"),
        pytest.param([2, 2, 2], 4, id="example_2"),
        pytest.param([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, id="leetcode_example"),
        pytest.param([1, 1], 1, id="two_bars"),
        pytest.param([0, 0], 0, id="zero_heights"),
        pytest.param([5, 0, 0, 0, 5], 20, id="tall_ends_win"),
        pytest.param([1, 2, 3, 4, 5], 6, id="increasing"),
        pytest.param([5, 4, 3, 2, 1], 6, id="decreasing"),
        pytest.param([1, 100, 100, 1], 100, id="tall_middle_beats_wide"),
        pytest.param([4, 3, 2, 1, 4], 16, id="short_bars_between"),
    ],
)
def test_max_area(method, heights, expected):
    assert getattr(Solution(), method)(heights) == expected
