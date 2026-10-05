"""
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise.
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Constraints:
  1 <= s1.length, s2.length <= 1000

Time Complexity: __, Memory Complexity: __
"""

from typing import List

import pytest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return False


# Add each new variant's method name here.
METHODS = ["checkInclusion"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        pytest.param("abc", "lecabee", True, id="example_1"),
        pytest.param("abc", "lecaabee", False, id="example_2"),
        pytest.param("ab", "eidbaooo", True, id="leetcode_example_1"),
        pytest.param("ab", "eidboaoo", False, id="leetcode_example_2"),
        pytest.param("a", "a", True, id="same_single_char"),
        pytest.param("abc", "ab", False, id="s1_longer_than_s2"),
        pytest.param("abc", "cba", True, id="whole_s2_is_permutation"),
        pytest.param("abc", "xxxbca", True, id="match_at_end"),
        pytest.param("abc", "cabxxx", True, id="match_at_start"),
        pytest.param("aab", "abbab", False, id="same_letters_wrong_counts"),
        pytest.param("aab", "xbaax", True, id="duplicate_letters"),
        pytest.param("abc", "acb", True, id="exact_length_shuffled"),
        pytest.param("ab", "a_b", False, id="letters_not_adjacent"),
    ],
)
def test_check_inclusion(method, s1, s2, expected):
    assert getattr(Solution(), method)(s1, s2) == expected
