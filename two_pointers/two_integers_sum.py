from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]


# print(Solution().twoSum([1, 2, 3, 4], 3))
print(Solution().twoSum([-5, -3, 0, 2, 4, 6, 8], 5))  # [2,7]
