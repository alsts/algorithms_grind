"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the i-th day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Constraints:
  1 <= prices.length <= 100
  0 <= prices[i] <= 100

Time Complexity: O(n), Memory Complexity: O(1)
"""

from typing import List

import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left(buy), right(sell)
        maxP = 0
        while r < len(prices):
            # check if profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # right pointer is lower, left pointer is always lowest value
                l = r  
            r += 1
        return maxP


# Add each new variant's method name here.
METHODS = ["maxProfit"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "prices, expected",
    [
        pytest.param([10, 1, 5, 6, 7, 1], 6, id="example_1"),
        pytest.param([10, 8, 7, 5, 2], 0, id="example_2_only_falling"),
        pytest.param([7, 1, 5, 3, 6, 4], 5, id="leetcode_example"),
        pytest.param([5], 0, id="single_day"),
        pytest.param([3, 3, 3], 0, id="flat"),
        pytest.param([1, 2], 1, id="two_days_up"),
        pytest.param([2, 1], 0, id="two_days_down"),
        pytest.param([1, 2, 3, 4, 5], 4, id="buy_first_sell_last"),
        pytest.param([2, 9, 1, 3], 7, id="min_after_best_sell"),
        pytest.param([3, 8, 1, 9], 8, id="new_min_gives_better_profit"),
        pytest.param([0, 100], 100, id="extreme_values"),
    ],
)
def test_max_profit(method, prices, expected):
    assert getattr(Solution(), method)(prices) == expected
