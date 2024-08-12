# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
from typing import List


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
