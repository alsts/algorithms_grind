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
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        # count each number
        num_counts = {}
        for num in nums:
            num_counts[num] = 1 + num_counts.get(num, 0)

        # push (counts, number) tuple to Max Heap:
        max_heap_by_count = []
        for num, counts in num_counts.items():
            tuple_count_num = (-1 * counts, num)  # negate to get Max Heap (heapq - is Min Heap)
            heapq.heappush(max_heap_by_count, tuple_count_num)  # first val in tuple would be used for sorting

        result = []
        for i in range(k):
            result.append(heapq.heappop(max_heap_by_count)[1])

        return result

    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        # count each number
        num_counts = {}
        for num in nums:
            num_counts[num] = 1 + num_counts.get(num, 0)

        # buckets sort
        buckets = [[] for i in range(len(nums) + 1)]  # +1 needed since counts would be represented by index
        for num, counts in num_counts.items():
            buckets[counts].append(num)

        # loop backwards in buckets to get the highest num counts first:
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # range (from, to, step)
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    result.append(num)

                    if len(result) == k:
                        return result

solution = Solution()
print(solution.topKFrequentBruteForce([1, 2, 2, 3, 3, 3], 2))
print(solution.topKFrequentBruteForce([7, 7], 1))

print(solution.topKFrequentHeap([1, 2, 2, 3, 3, 3], 2))
print(solution.topKFrequentHeap([7, 7], 1))

print(solution.topKFrequentBucketSort([1, 2, 2, 3, 3, 3], 2))
print(solution.topKFrequentBucketSort([7, 7], 1))
