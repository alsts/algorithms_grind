from collections import defaultdict
from typing import List


# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Time Complexity: O(n*m) n->words, m->average letters in words, Memory Complexity: O(n)
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # 26 possible characters - only lowercase English letters
            letters_count = [0 for i in range(0, 26)]  # a, [0] * 26

            for letter in word:
                letter_slot = ord(letter) - ord('a')
                letters_count[letter_slot] += 1

            anagrams[tuple(letters_count)].append(word)

        return list(anagrams.values())


    def groupAnagramsBruteForce(self, strs: List[str]) -> List[List[str]]:

        anagrams = []

        for i, word in enumerate(strs):
            word_chars = self.helper(word)

            if not self.helper2(anagrams, word, word_chars):
                anagrams.append([word])

        return anagrams

    def helper2(self, anagrams, word, word_chars):
        for an_group in anagrams:
            an_group_word = an_group[0]

            if len(word) != len(an_group_word):
                continue

            an_group_word_chars = self.helper(an_group_word)

            if an_group_word_chars == word_chars:
                an_group.append(word)
                return True

    def helper(self, word):
        word_chars = {}
        for j, char in enumerate(word):
            word_chars[char] = 1 + word_chars.get(char, 0)
        return word_chars


solution = Solution()

print(solution.groupAnagrams(
    ["act", "pots", "tops", "cat", "stop", "hat"]))  # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
