"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
  1. Every open bracket is closed by the same type of close bracket.
  2. Open brackets are closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Constraints:
  1 <= s.length <= 1000

Time Complexity: O(n), Memory Complexity: O(n)

Notes:
  - Stack holds unclosed openers; top (stack[-1]) = the one that must close next.
  - Closer → top must be its matching opener → pop; empty stack or wrong type → False.
  - closeToOpen maps closer → opener, so one lookup checks both "is closer" and "which opener".
  - End: stack must be empty, or some opener was never closed ("((").
  - `if stack` = non-empty; pop() removes and returns stack[-1], O(1).
"""

from typing import List

import pytest


class Solution:
    def isValidBrute(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""

    def isValid(self, s: str) -> bool:
        stack = []  # unclosed openers, top = most recent
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:  # closing bracket
                if stack and stack[-1] == closeToOpen[c]:  # non-empty and top matches
                    stack.pop()  # remove top (stack[-1])
                else:
                    return False  # nothing to close or wrong type
            else:
                stack.append(c)  # opener → push on top

        return not stack  # empty → every opener was closed


# Add each new variant's method name here.
METHODS = ["isValid"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "s, expected",
    [
        pytest.param("[]", True, id="example_1"),
        pytest.param("([{}])", True, id="example_2_nested"),
        pytest.param("[(])", False, id="example_3_wrong_order"),
        pytest.param("()[]{}", True, id="leetcode_example_sequence"),
        pytest.param("(]", False, id="leetcode_example_mismatch"),
        pytest.param("(", False, id="single_open"),
        pytest.param(")", False, id="single_close_empty_stack"),
        pytest.param("((", False, id="unclosed_left_over"),
        pytest.param("())", False, id="extra_close"),
        pytest.param("){", False, id="close_before_open"),
        pytest.param("{[]}()", True, id="nested_then_sequence"),
        pytest.param("((((((()))))))", True, id="deep_nesting"),
        pytest.param("[({})](]", False, id="valid_prefix_then_bad"),
    ],
)
def test_is_valid(method, s, expected):
    assert getattr(Solution(), method)(s) == expected
