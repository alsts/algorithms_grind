from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build prefix product array
        prefix_p = [0] * len(nums)
        prefix_p[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_p[i] = prefix_p[i - 1] * nums[i]

        # build postfix product array
        postfix_p = [0] * len(nums)
        postfix_p[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):  # loop backwards
            postfix_p[i] = postfix_p[i + 1] * nums[i]

        result = []
        for i in range(len(nums)):
            # prefix and postfix of value
            prefix = prefix_p[i - 1] if i > 0 else 1
            postfix = postfix_p[i + 1] if i + 1 < len(nums) else 1

            result.append(prefix * postfix)

        return result

    def productExceptSelfOptimised(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # build prefix product array [1,1,2,6], shifted by 1 right
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        # multiply by postfix product array shifted by 1 left
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


solution = Solution()

# prefix arr:  [1,   2,  6, 24]
# postfix arr: [24, 24, 12, 4 ]
# For example: for i = 1 -> prefix before i = 1, postfix after i = 12
# result: [1*24, 1 * 12, 2*4, 6 * 1]
print(solution.productExceptSelfOptimised([1,2,3,4]))
