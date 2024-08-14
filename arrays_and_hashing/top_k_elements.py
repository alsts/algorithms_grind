# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
import heapq
from typing import List


class Solution:

    # Time Complexity: O(n * k), Memory Complexity: O(n)
    def topKFrequentBruteForce(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        k_set = set()
        count = {}
        # min heap?

        for n in nums:
            frequency_map[n] = 1 + frequency_map.get(n, 0)

            if len(k_set) < k:
                k_set.add(n)
            elif n in k_set:
                continue
            else:
                for k_item in k_set:
                    if frequency_map[k_item] < frequency_map[n]:
                        k_set.remove(k_item)
                        k_set.add(n)
                        break

        return list(k_set)

    # Time Complexity: O(k log n), Memory Complexity: O(n)
    def topKFrequentMaxHeap(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        heap = []

        for n in nums:
            frequency_map[n] = 1 + frequency_map.get(n, 0)

        for key, val in frequency_map.items():
            heapq.heappush(heap, (key * -1, val))

        most_frequent_items = []
        for _ in range(k):
            most_frequent_items.append(heapq.heappop(heap)[1])

        return most_frequent_items

    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq_buckets = [[] for i in range(0, len(nums) + 1)]  # max bucket can be the size of nums

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        for num, count in counts.items():
            freq_buckets[count].append(num)

        res = []

        # loop through buckets in reverse order:
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


solution = Solution()
print(solution.topKFrequentBruteForce([1, 2, 2, 3, 3, 3], 2))
print(solution.topKFrequentBruteForce([7, 7], 1))

print(solution.topKFrequentMaxHeap([1, 2, 2, 3, 3, 3], 2))
print(solution.topKFrequentMaxHeap([7, 7], 1))

print(solution.topKFrequentBucketSort([1, 2, 2, 3, 3, 3], 2))
print(solution.topKFrequentBucketSort([7, 7], 1))
