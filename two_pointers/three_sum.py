from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, n in enumerate(nums):
            # optimisation - exit loop early since no numbers would sum up to 0
            if n > 0:
                break

            # skip duplicates:
            if i > 0 and nums[i - 1] == n:
                continue

            # cover remaining slots using two sum:
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # sum found
                    result.append([n, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # shift left pointer if duplicate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
