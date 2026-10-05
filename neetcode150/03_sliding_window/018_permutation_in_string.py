"""
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise.
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Constraints:
  1 <= s1.length, s2.length <= 1000

n = len(s2), m = len(s1)

checkInclusionBrute    Time: O(n·m)        Memory: O(1)  (26 counts)
checkInclusionGrow     Time: O(n·m)        Memory: O(1)  (stops early, faster in practice)
checkInclusionSliding  Time: O(26·n) = O(n)  Memory: O(1)
checkInclusion         Time: O(n)          Memory: O(1)

Notes:
  - Permutation of s1 = same letter counts → fixed-size window of len(s1).
  - Slice end is excluded: s2[l:r] → loop r up to len(s2) inclusive, or the last window is missed.
  - Brute rebuilds counts per window → O(m) each. Sliding: +1 entering char, -1 leaving char → O(1).
  - Grow (NeetCode): from each start, grow until a letter goes over its count → break; cur == need → found.
  - Sliding still compares 26 counts per step; matches tracks how many letters are equal → O(1) per step.
  - matches only changes when a count crosses equality: hits it (+1) or leaves it by one (-1).
  - len(s1) > len(s2) → False up front.
"""

from typing import List

import pytest


class Solution:
    def checkInclusionBrute(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26  # slot 0..25 = 'a'..'z'
        for c in s1:
            s1_count[ord(c) - ord("a")] += 1

        for r in range(len(s1), len(s2) + 1):  # + 1: slice end is excluded
            l = r - len(s1)
            window = [0] * 26  # rebuilt every window → O(m)
            for c in s2[l:r]:
                window[ord(c) - ord("a")] += 1

            if window == s1_count:
                return True

        return False

    def checkInclusionGrow(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)  # distinct letters that must hit their exact count
        for i in range(len(s2)):  # try every start
            count2, cur = {}, 0  # cur = letters at exact count
            for j in range(i, len(s2)):  # grow the window
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:  # too many (or not in s1) → this start is dead
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:  # letter just reached its exact count
                    cur += 1
                if cur == need:  # all letters exact, none over → permutation
                    return True
        return False

    def checkInclusionSliding(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, window = [0] * 26, [0] * 26  # slot 0..25 = 'a'..'z'
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1  # letters of s1
            window[ord(s2[i]) - ord("a")] += 1  # first window: s2[0:len(s1)]

        if window == s1_count:  # first window already a match
            return True

        for r in range(len(s1), len(s2)):  # slide by one: add right, drop left
            window[ord(s2[r]) - ord("a")] += 1  # char entering
            window[ord(s2[r - len(s1)]) - ord("a")] -= 1  # char leaving, len(s1) behind
            if window == s1_count:  # O(26)
                return True

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, window = [0] * 26, [0] * 26
        for i in range(len(s1)):  # first window
            s1_count[ord(s1[i]) - ord("a")] += 1
            window[ord(s2[i]) - ord("a")] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == window[i])  # letters with equal count

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add right char
            i = ord(s2[r]) - ord("a")
            window[i] += 1
            if window[i] == s1_count[i]:
                matches += 1  # just became equal
            elif window[i] == s1_count[i] + 1:
                matches -= 1  # was equal, now one too many

            # drop left char
            i = ord(s2[r - len(s1)]) - ord("a")
            window[i] -= 1
            if window[i] == s1_count[i]:
                matches += 1  # just became equal
            elif window[i] == s1_count[i] - 1:
                matches -= 1  # was equal, now one too few

        return matches == 26  # last window


# Add each new variant's method name here.
METHODS = ["checkInclusionBrute", "checkInclusionGrow", "checkInclusionSliding", "checkInclusion"]


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
