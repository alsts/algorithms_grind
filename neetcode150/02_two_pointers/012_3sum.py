"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where
nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Constraints:
  3 <= nums.length <= 1000
  -10^5 <= nums[i] <= 10^5

Time Complexity: O(n²), Memory Complexity: O(1) (sort in place; output doesn't count)

Notes:
  - Sort O(n log n), then for each i run Two Sum II on the rest → n × n = O(n²), which dominates.
  - num > 0 → break: sorted, so nothing to the right can bring the sum back to 0.
  - Skip duplicate i (nums[i] == nums[i - 1]) and duplicate l after a hit → no repeated triplets.
"""

from typing import List

import pytest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            # no point of checking of > 0, in sorted arr
            if num > 0:
                break

            # duplicate
            if i > 0 and nums[i - 1] == num:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # sum found
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # duplicate left second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result


# Add each new variant's method name here.
METHODS = ["threeSum"]


# Triplets and their order don't matter, so compare sorted.
def normalise(triplets: List[List[int]]) -> List[List[int]]:
    return sorted(sorted(t) for t in triplets)


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]], id="example_1"),
        pytest.param([0, 1, 1], [], id="example_2_no_triplet"),
        pytest.param([0, 0, 0], [[0, 0, 0]], id="example_3_all_zeros"),
        pytest.param([0, 0, 0, 0, 0], [[0, 0, 0]], id="many_zeros_one_triplet"),
        pytest.param([-2, 0, 0, 2, 2], [[-2, 0, 2]], id="duplicate_triplets_removed"),
        pytest.param([1, 2, 3, 4], [], id="all_positive"),
        pytest.param([-4, -3, -2, -1], [], id="all_negative"),
        pytest.param([3, -2, 1, 0], [], id="no_zero_sum"),
        pytest.param([-1, -1, 2, 2], [[-1, -1, 2]], id="same_value_twice_in_triplet"),
        pytest.param(
            [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
            id="many_duplicates",
        ),
    ],
)
def test_three_sum(method, nums, expected):
    assert normalise(getattr(Solution(), method)(nums)) == normalise(expected)
