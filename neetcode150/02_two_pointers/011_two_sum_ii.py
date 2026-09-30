"""
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number
and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Constraints:
  2 <= numbers.length <= 1000
  -1000 <= numbers[i] <= 1000
  -1000 <= target <= 1000

Time Complexity: O(n), Memory Complexity: O(1)

Notes:
  - Sorted → two pointers: sum too small → l += 1, too big → r -= 1.
  - Each step drops one element for good → at most n steps.
  - Answer is 1-indexed → return [l + 1, r + 1].
  - Hashmap (003) also works but is O(n) memory → breaks the O(1) rule.
"""

from typing import List

import pytest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []


# Add each new variant's method name here.
METHODS = ["twoSum"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        pytest.param([1, 2, 3, 4], 3, [1, 2], id="example_1"),
        pytest.param([2, 7, 11, 15], 9, [1, 2], id="leetcode_example_1"),
        pytest.param([2, 3, 4], 6, [1, 3], id="leetcode_example_2"),
        pytest.param([-1, 0], -1, [1, 2], id="leetcode_example_3"),
        pytest.param([5, 25], 30, [1, 2], id="two_elements"),
        pytest.param([1, 3, 4, 4], 8, [3, 4], id="duplicates_are_the_answer"),
        pytest.param([1, 2, 3, 4, 5, 6], 11, [5, 6], id="answer_at_end"),
        pytest.param([-5, -3, 0, 2, 9], -8, [1, 2], id="negatives"),
        pytest.param([-3, 1, 2, 3], 0, [1, 4], id="zero_target"),
        pytest.param([1, 2, 3, 5, 7], 6, [1, 4], id="does_not_reuse_middle_element"),
    ],
)
def test_two_sum_ii(method, numbers, target, expected):
    assert getattr(Solution(), method)(numbers, target) == expected
