"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Time Complexity: O(n), Space Complexity: O(n)
"""

from typing import List, Optional


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
            
        return False

# Paste the examples from the problem, then: uv run pytest neetcode150/01_arrays_hashing/001_contains_duplicate.py
def test_example_1():
    solution = Solution()
    assert solution.hasDuplicate([1, 2, 3, 4, 1]) is True

def test_example_2():
    solution = Solution()
    assert solution.hasDuplicate([1, 2, 3, 4]) is False
