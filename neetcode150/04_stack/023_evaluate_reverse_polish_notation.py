"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.

  - The operands may be integers or the results of other operations.
  - The operators include '+', '-', '*', and '/'.
  - Assume that division between integers always truncates toward zero.

Constraints:
  1 <= tokens.length <= 1000
  tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].

Time Complexity: O(n), Memory Complexity: O(n)

Notes:
  - Number → push. Operator → pop two, apply, push result back.
  - First pop is the RIGHT operand: "5 3 -" → 5 - 3, not 3 - 5. Matters for - and /.
  - Divide with int(b / a), not b // a: // floors (-7 // 2 = -4), problem wants toward zero (-3).
  - "-7" is a number, not the "-" operator → compare tokens with ==, not `in`.
  - Each token pushed/popped at most once → O(n); stack can hold up to n numbers → O(n).
"""

from typing import List

import pytest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # numbers waiting for an operator
        for c in tokens:
            if c == "+":
                stack.append(int(stack.pop() + stack.pop()))  # order doesn't matter
            elif c == "-":
                a, b = stack.pop(), stack.pop()  # a = right operand (popped first), b = left
                stack.append(int(b - a))
            elif c == "*":
                stack.append(int(stack.pop() * stack.pop()))  # order doesn't matter
            elif c == "/":
                a, b = stack.pop(), stack.pop()  # a = right operand (popped first), b = left
                stack.append(int(b / a))  # int() truncates toward zero; // would floor
            else:
                stack.append(int(c))  # number (incl. "-7") → push
        return stack[0]  # valid RPN leaves exactly one value


# Add each new variant's method name here.
METHODS = ["evalRPN"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "tokens, expected",
    [
        pytest.param(["1", "2", "+", "3", "*", "4", "-"], 5, id="example_1"),
        pytest.param(["2", "1", "+", "3", "*"], 9, id="leetcode_example_1"),
        pytest.param(["4", "13", "5", "/", "+"], 6, id="leetcode_example_2"),
        pytest.param(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22, id="leetcode_example_3"
        ),
        pytest.param(["42"], 42, id="single_number"),
        pytest.param(["-7"], -7, id="single_negative_number"),
        pytest.param(["5", "3", "-"], 2, id="subtract_order"),
        pytest.param(["3", "5", "-"], -2, id="subtract_negative_result"),
        pytest.param(["7", "2", "/"], 3, id="divide_order"),
        pytest.param(["-7", "2", "/"], -3, id="divide_truncates_toward_zero"),
        pytest.param(["7", "-2", "/"], -3, id="divide_negative_divisor"),
        pytest.param(["1", "3", "/"], 0, id="divide_to_zero"),
        pytest.param(["-3", "-4", "*"], 12, id="negative_times_negative"),
    ],
)
def test_eval_rpn(method, tokens, expected):
    assert getattr(Solution(), method)(tokens) == expected
