"""
001. Contains Duplicate (Arrays & Hashing)
NeetCode: https://neetcode.io/solutions/contains-duplicate
LeetCode: https://leetcode.com/problems/contains-duplicate/

Started: 2026-09-25   Minutes: __   Result: ☐ ✅ solo · 🟡 hint · 🔴 read solution

Say it out loud first:
  brute force:
  optimal:
  time / space:
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
