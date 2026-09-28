"""
Given an integer array nums, return an array output where output[i] is the product
of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: solve it in O(n) time without using the division operation.

Constraints:
  2 <= nums.length <= 1000
  -20 <= nums[i] <= 20

productExceptSelfBrute              Time: O(n²)  Memory: O(1)
productExceptSelfDynamic            Time: O(n)   Memory: O(n)
productExceptSelfDynamicOptimised   Time: O(n)   Memory: O(1)  (output array doesn't count)

Notes:
  - output[i] = prefix[i - 1] × postfix[i + 1], use 1 at the edges.
  - Products start at 1 (sums at 0). Overwrite with =, combine with *=.
  - Optimised: use running value first, then multiply in nums[i] → self never included.
"""

from typing import List

import pytest


class Solution:
    def productExceptSelfBrute(self, nums: List[int]) -> List[int]:
        products = []
        current_num = 0
        while current_num < len(nums):
            product = 1

            for i, num in enumerate(nums):
                if i != current_num:
                    product *= num

            products.append(product)
            current_num += 1

        return products

    # output[i] = (product of everything LEFT of i) × (product of everything RIGHT of i) = prefix[i - 1] × postfix[i + 1]
    # prefix arr:  [1,   2,  6, 24]
    # postfix arr: [24, 24, 12, 4 ]
    # For example: for i = 1 -> prefix before i = 1, postfix after i = 12
    # result: [1*24, 1 * 12, 2*4, 6 * 1]
    def productExceptSelfDynamic(self, nums: List[int]) -> List[int]:
        result = []

        prefix_arr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            prefix_arr[i] = prefix

        postfix_arr = [1] * len(nums)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix *= nums[i]
            postfix_arr[i] = postfix

        for i in range(len(nums)):
            prefix_i = prefix_arr[i - 1] if i > 0 else 1
            postfix_i = postfix_arr[i + 1] if i + 1 < len(nums) else 1
            result.append(prefix_i * postfix_i)

        return result

    def productExceptSelfDynamicOptimised(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix 
            prefix *= nums[i] # this value delays for next cycle - prefix criteria (i - 1)

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix # update prefix results with postfix
            postfix *= nums[i] # postfix criteria (i + 1) + we going backwards

        return result


METHODS = ["productExceptSelfBrute", "productExceptSelfDynamic", "productExceptSelfDynamicOptimised"]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([1, 2, 4, 6], [48, 24, 12, 8], id="example_1"),
        pytest.param([-1, 0, 1, 2, 3], [0, -6, 0, 0, 0], id="example_2"),
        pytest.param([3, 4], [4, 3], id="two_elements"),
        pytest.param([0, 0, 5], [0, 0, 0], id="two_zeros"),
        pytest.param([0, 4, 5], [20, 0, 0], id="zero_at_start"),
        pytest.param([2, 3, 0], [0, 0, 6], id="zero_at_end"),
        pytest.param([-2, -3, 4], [-12, -8, 6], id="negatives"),
        pytest.param([1, 1, 1, 1], [1, 1, 1, 1], id="all_ones"),
        pytest.param([20] * 7 + [1], [20**6] * 7 + [20**7], id="large_products"),
    ],
)
def test_product_except_self(method, nums, expected):
    assert getattr(Solution(), method)(nums) == expected
