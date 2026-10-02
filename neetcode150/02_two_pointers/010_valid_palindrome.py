"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Constraints:
  1 <= s.length <= 1000
  s is made up of only printable ASCII characters.

Time Complexity: O(n), Memory Complexity: O(1)

Notes:
  - Two pointers from both ends; skip non-alphanumeric, compare .lower().
  - Inner loops keep l < r so skipping can't run past the middle.
  - Loop ends with no mismatch → return True.
  - Alt: clean = [c.lower() for c in s if c.isalnum()]; clean == clean[::-1] → O(n) memory.
"""

from typing import List

import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlNum(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        

# Add each new variant's method name here.
METHODS = ["isPalindrome"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "s, expected",
    [
        pytest.param("Was it a car or a cat I saw?", True, id="example_1"),
        pytest.param("tab a cat", False, id="example_2"),
        pytest.param("A man, a plan, a canal: Panama", True, id="leetcode_example"),
        pytest.param(" ", True, id="only_space"),
        pytest.param(".,!?", True, id="only_symbols"),
        pytest.param("a", True, id="single_char"),
        pytest.param("Aa", True, id="case_insensitive"),
        pytest.param("ab", False, id="two_different"),
        pytest.param("0P", False, id="digit_vs_letter"),
        pytest.param("1a2 2A1", True, id="digits_count"),
        pytest.param("a.", True, id="symbol_at_end"),
        pytest.param(".,a", True, id="symbols_at_start"),
        pytest.param("race a car", False, id="almost_palindrome"),
    ],
)
def test_is_palindrome(method, s, expected):
    assert getattr(Solution(), method)(s) == expected
