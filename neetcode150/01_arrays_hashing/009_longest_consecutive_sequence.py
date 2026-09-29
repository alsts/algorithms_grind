"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Constraints:
  0 <= nums.length <= 1000
  -10^9 <= nums[i] <= 10^9

longestConsecutive (count up from every num)  Time: O(n²)  Memory: O(n)
Target: O(n) time, O(n) memory.

Notes:
  - set(nums) is O(n) to build, `x in set` is O(1) on average.
  - Counting up from every num recounts the same run → [1..5] costs 4 + 3 + 2 + 1 checks.
  - Fix: only count from the start of a run → each num counted once → O(n).
"""

from typing import List

import pytest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_count = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set:
                count = 1

                while num + count in nums_set:
                    count += 1

                seq_count = max(count, seq_count)

        return seq_count


# Add each new variant's method name here.
METHODS = ["longestConsecutive"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([2, 20, 4, 10, 3, 4, 5], 4, id="example_1"),
        pytest.param([0, 3, 2, 5, 4, 6, 1, 1], 7, id="example_2"),
        pytest.param([], 0, id="empty"),
        pytest.param([7], 1, id="single_element"),
        pytest.param([1, 1, 1], 1, id="all_duplicates"),
        pytest.param([10, 30, 20], 1, id="no_neighbours"),
        pytest.param([5, 4, 3, 2, 1], 5, id="reversed"),
        pytest.param([-2, -1, 0, 1], 4, id="negatives_through_zero"),
        pytest.param([1, 2, 3, 100, 101, 102, 103], 4, id="longest_is_second_run"),
        pytest.param([10**9, -(10**9), 10**9 - 1], 2, id="extreme_values"),
    ],
)
def test_longest_consecutive(method, nums, expected):
    assert getattr(Solution(), method)(nums) == expected
