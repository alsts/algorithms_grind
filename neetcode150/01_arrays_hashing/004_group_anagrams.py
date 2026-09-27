"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

strs[i] is made up of lowercase English letters! ****

Time Complexity: O(n*m) n->words, m->average letters in words, Memory Complexity: O(n)
"""

from collections import defaultdict
from typing import List

import pytest


class Solution:
    # O(n · m log m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       groups: defaultdict = defaultdict(list) 
       for str in strs:
           groups["".join(sorted(str))].append(str)
       
       return list(groups.values()) 

    # O(n * m)
    def groupAnagramsTricky(self, strs: List[str]) -> List[List[str]]:
       groups: defaultdict = defaultdict(list) 

       for str in strs:
           letters_count = [0 for i in range(0, 26)] # a - z

           for letter in str:
              letter_pos = ord(letter) - ord('a') # ord('z') - ord('a')  122 - 97 = 25 
              letters_count[letter_pos] += 1 

           groups[tuple(letters_count)].append(str) 
        
       
       return list(groups.values()) 
       
       
# Groups and words inside them can come back in any order, so compare sorted.
def normalise(groups: List[List[str]]) -> List[List[str]]:
    return sorted(sorted(group) for group in groups)


METHODS = ["groupAnagrams", "groupAnagramsTricky"]


@pytest.mark.parametrize("method", METHODS)
def test_example_1(method):
    result = getattr(Solution(), method)(["act", "pots", "tops", "cat", "stop", "hat"])
    assert normalise(result) == normalise([["hat"], ["act", "cat"], ["stop", "pots", "tops"]])


@pytest.mark.parametrize("method", METHODS)
def test_single_word(method):
    assert normalise(getattr(Solution(), method)(["x"])) == [["x"]]


@pytest.mark.parametrize("method", METHODS)
def test_empty_string(method):
    assert normalise(getattr(Solution(), method)([""])) == [[""]]


@pytest.mark.parametrize("method", METHODS)
def test_same_letters_different_counts_are_not_anagrams(method):
    result = getattr(Solution(), method)(["aab", "abb", "bab"])
    assert normalise(result) == normalise([["aab"], ["abb", "bab"]])


@pytest.mark.parametrize("method", METHODS)
def test_duplicates_stay_in_same_group(method):
    result = getattr(Solution(), method)(["eat", "tea", "eat"])
    assert normalise(result) == [["eat", "eat", "tea"]]
