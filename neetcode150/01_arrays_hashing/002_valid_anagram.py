"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Time Complexity: O(n), Space Complexity: O(n)
"""

from typing import List, Optional


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = {}
        t_counts = {}

        for n in range(len(s)):
            s_counts[s[n]] = s_counts.get(s[n], 0) + 1

        for n in range(len(t)):
            t_counts[t[n]] = t_counts.get(t[n], 0) + 1

        return s_counts == t_counts    

# Paste the examples from the problem, then: uv run pytest neetcode150/01_arrays_hashing/002_valid_anagram.py
def test_example_1():
    assert Solution().isAnagram("anagram", "nagaram") is True


def test_example_2():
    assert Solution().isAnagram("rat", "car") is False


def test_different_lengths():
    assert Solution().isAnagram("ab", "abc") is False


def test_same_letters_different_counts():
    assert Solution().isAnagram("aab", "abb") is False
