from typing import List


# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)

        return False


solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 3]))
print(solution.hasDuplicate([1, 2, 3, 4]))
