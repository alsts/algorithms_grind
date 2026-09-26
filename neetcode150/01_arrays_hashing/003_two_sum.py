"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Time Complexity: O(n), Memory Complexity: O(n)
"""

from typing import List, Optional


class Solution:
    def sumTwo(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, n in enumerate(nums):
            if target - n in visited:
                return [visited[target - n], i]
            visited[n] = i

        return [1, 2]


# Paste the examples from the problem, then: uv run pytest neetcode150/01_arrays_hashing/003_two_sum.py
def test_example_1():
    assert Solution().sumTwo([1, 2, 3, 4], 3) == [0, 1]


def test_example_2():
    assert Solution().sumTwo([3, 4, 5, 6], 7) == [0, 1]


def test_example_3():
    assert Solution().sumTwo([4, 5, 6], 10) == [0, 2]


def test_duplicates():
    assert Solution().sumTwo([5, 5], 10) == [0, 1]


def test_negatives():
    assert Solution().sumTwo([-3, 4, 3, 90], 0) == [0, 2]


def test_does_not_reuse_same_element():
    assert Solution().sumTwo([3, 2, 4], 6) == [1, 2]
