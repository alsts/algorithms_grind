from typing import List


# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Time Complexity: O(n), Memory Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashset:
                return [hashset[diff], i]
            hashset[nums[i]] = i


solution = Solution()
print(solution.twoSum([3, 4, 5, 6], 7))
print(solution.twoSum([4, 5, 6], 10))
print(solution.twoSum([5, 5], 10))
