"""
Given two strings s and t, return the shortest substring of s such that every character in t,
including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Constraints:
  1 <= s.length, t.length <= 1000
  s and t consist of uppercase and lowercase English letters.

Time Complexity: __, Memory Complexity: __
"""

from typing import List

import pytest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return ""


# Add each new variant's method name here.
METHODS = ["minWindow"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "s, t, expected",
    [
        pytest.param("OUZODYXAZV", "XYZ", "YXAZ", id="example_1"),
        pytest.param("xyz", "xyz", "xyz", id="example_2_whole_string"),
        pytest.param("x", "xy", "", id="example_3_t_longer"),
        pytest.param("ADOBECODEBANC", "ABC", "BANC", id="leetcode_example_1"),
        pytest.param("a", "a", "a", id="single_char"),
        pytest.param("a", "aa", "", id="needs_duplicate_not_there"),
        pytest.param("abc", "d", "", id="char_missing"),
        pytest.param("baaab", "aa", "aa", id="t_has_duplicates"),
        pytest.param("abbbbbbac", "abc", "bac", id="later_window_shorter"),
        pytest.param("aA", "A", "A", id="case_sensitive"),
        pytest.param("cabwefgewcwaefgcf", "cae", "cwae", id="shrink_past_extras"),
        pytest.param("bba", "ab", "ba", id="match_at_end"),
    ],
)
def test_min_window(method, s, t, expected):
    assert getattr(Solution(), method)(s, t) == expected
