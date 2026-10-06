"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge
of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

Constraints:
  1 <= nums.length <= 10^5
  -10^4 <= nums[i] <= 10^4
  1 <= k <= nums.length

Time Complexity: __, Memory Complexity: __
"""

from typing import List

import pytest


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return []


# Add each new variant's method name here.
METHODS = ["maxSlidingWindow"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        pytest.param([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6], id="example_1"),
        pytest.param([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7], id="leetcode_example_1"),
        pytest.param([1], 1, [1], id="leetcode_example_2_single"),
        pytest.param([4, 2, 7], 1, [4, 2, 7], id="k_one_returns_input"),
        pytest.param([4, 2, 7, 1], 4, [7], id="k_equals_length"),
        pytest.param([5, 4, 3, 2, 1], 2, [5, 4, 3, 2], id="decreasing_max_leaves_window"),
        pytest.param([1, 2, 3, 4, 5], 2, [2, 3, 4, 5], id="increasing"),
        pytest.param([3, 3, 3, 3], 2, [3, 3, 3], id="all_equal"),
        pytest.param([-7, -8, 7, 5, 7, 1, 6, 0], 4, [7, 7, 7, 7, 7], id="duplicate_max"),
        pytest.param([-1, -5, -3], 2, [-1, -3], id="negatives"),
        pytest.param([9, 1, 1, 1, 1], 3, [9, 1, 1], id="big_value_expires"),
    ],
)
def test_max_sliding_window(method, nums, k, expected):
    assert getattr(Solution(), method)(nums, k) == expected
