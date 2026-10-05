"""
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Constraints:
  0 <= s.length <= 1000
  s may consist of printable ASCII characters.

m = distinct chars (≤ 95 printable ASCII)

lengthOfLongestSubstringBrute  Time: O(n·m)  Memory: O(m)
lengthOfLongestSubstring       Time: O(n)    Memory: O(m)
lengthOfLongestSubstringFor    Time: O(n)    Memory: O(m)

Notes:
  - Brute: from every start i, grow until a repeat → at most m steps before a repeat.
  - Window [l, r] always has unique chars; set mirrors exactly s[l..r].
  - Duplicate at r → shrink from the left until it's gone, then add s[r].
  - O(n): r moves n times, l moves at most n times total (never goes back).
  - Don't pre-add s[0]; r is the next char to add → start r = 0, set empty.
  - Loop through every index: r < len(s) or range(len(s)), not len(s) - 1.
"""

from typing import List

import pytest


class Solution:
    def lengthOfLongestSubstringBrute(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:  # repeat → this start is done
                    break
                seen.add(s[j])
            res = max(res, len(seen))
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        char_set = set()

        while r < len(s):
            while s[r] in char_set: # duplicate found -> remove until not present
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            res = max(res, len(char_set))
            r += 1

        return res

    def lengthOfLongestSubstringFor(self, s: str) -> int:
        res = 0
        l = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:  # duplicate → shrink from the left
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            res = max(res, r - l + 1)  # window size

        return res


# Add each new variant's method name here.
METHODS = ["lengthOfLongestSubstringBrute", "lengthOfLongestSubstring", "lengthOfLongestSubstringFor"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "s, expected",
    [
        pytest.param("zxyzxyz", 3, id="example_1"),
        pytest.param("xxxx", 1, id="example_2_all_same"),
        pytest.param("abcabcbb", 3, id="leetcode_example_1"),
        pytest.param("pwwkew", 3, id="leetcode_example_3_substring_not_subsequence"),
        pytest.param("", 0, id="empty"),
        pytest.param(" ", 1, id="single_space"),
        pytest.param("abcdef", 6, id="all_unique"),
        pytest.param("abba", 2, id="left_must_not_move_back"),
        pytest.param("dvdf", 3, id="restart_after_repeat"),
        pytest.param("tmmzuxt", 5, id="repeat_far_behind_left"),
        pytest.param("a b!a", 4, id="spaces_and_symbols"),
    ],
)
def test_length_of_longest_substring(method, s, expected):
    assert getattr(Solution(), method)(s) == expected
