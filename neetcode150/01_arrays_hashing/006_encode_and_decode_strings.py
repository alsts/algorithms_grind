"""
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Implement encode and decode.

Constraints:
  0 <= strs.length < 100
  0 <= strs[i].length < 200
  strs[i] contains only UTF-8 characters.

Time Complexity: O(n), Memory Complexity: O(n)
"""

from typing import List

import pytest


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # select the number of letters in encoded word
            while s[j] != "#":
                j += 1 # j == #

            word_len = int(s[i:j])
            i = j + 1  # word start
            j = i + word_len  # word end

            decoded.append(s[i:j])
            i = j

        return decoded


# Round trip: decode(encode(x)) must give back x exactly.
@pytest.mark.parametrize(
    "strs",
    [
        pytest.param(["neet", "code", "love", "you"], id="example_1"),
        pytest.param(["we", "say", ":", "yes"], id="example_2"),
        pytest.param([], id="empty_list"),
        pytest.param([""], id="one_empty_string"),
        pytest.param(["", "", ""], id="many_empty_strings"),
        pytest.param(["a#b", "#", "3#abc"], id="delimiter_inside_strings"),
        pytest.param(["12", "4#", "#12"], id="digits_and_delimiters"),
        pytest.param(["x" * 199, "y"], id="long_string_two_digit_length"),
        pytest.param(["hello world", " ", "tab\there"], id="spaces_and_tabs"),
        pytest.param(["héllo", "日本", "🙂"], id="unicode"),
    ],
)
def test_round_trip(strs):
    s = Solution()
    assert s.decode(s.encode(strs)) == strs


def test_encode_returns_single_string():
    assert isinstance(Solution().encode(["a", "b"]), str)
