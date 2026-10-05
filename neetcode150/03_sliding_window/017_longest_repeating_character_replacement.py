"""
You are given a string s consisting of only uppercase English characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Constraints:
  1 <= s.length <= 1000
  0 <= k <= s.length

Time Complexity: __, Memory Complexity: __
"""

from typing import List

import pytest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return 0


# Add each new variant's method name here.
METHODS = ["characterReplacement"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "s, k, expected",
    [
        pytest.param("XYYX", 2, 4, id="example_1"),
        pytest.param("AAABABB", 1, 5, id="example_2"),
        pytest.param("ABAB", 2, 4, id="leetcode_example_1"),
        pytest.param("AABABBA", 1, 4, id="leetcode_example_2"),
        pytest.param("A", 0, 1, id="single_char"),
        pytest.param("ABCD", 0, 1, id="k_zero_all_different"),
        pytest.param("AABBB", 0, 3, id="k_zero_longest_run"),
        pytest.param("AAAA", 2, 4, id="already_uniform"),
        pytest.param("ABCDE", 5, 5, id="k_equals_length"),
        pytest.param("ABBBCBBB", 1, 7, id="replace_middle_char"),
        pytest.param("BAAAB", 2, 5, id="replace_both_ends"),
    ],
)
def test_character_replacement(method, s, k, expected):
    assert getattr(Solution(), method)(s, k) == expected
