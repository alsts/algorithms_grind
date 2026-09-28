"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

n = len(nums), m = distinct values

topKFrequent            Time: O(n + m log m)      Memory: O(m)
topKFrequentTiny        Time: O(n + m + k log m)  Memory: O(m)
topKFrequentBucketSort  Time: O(n)                Memory: O(n)

Notes:
  - Heap: push (-count, num) for max-heap; heapify is O(m) vs m pushes O(m log m).
  - Bucket sort: index = frequency, max freq = n → n + 1 buckets.
  - Bucket scan is O(n + m) not O(n·m): each num sits in exactly one bucket.
"""

import heapq
from collections import Counter, defaultdict
from typing import List

import pytest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        # Counting: O(n)
        for num in nums:
            counts[num] += 1

        # m pushes: O(m log m)
        max_heap_by_counts = []
        for item, count in counts.items():
            val = (-1 * count, item)
            heapq.heappush(max_heap_by_counts, val)

        # k pops: O(k log m)
        result = []
        while len(result) != k:
            result.append(heapq.heappop(max_heap_by_counts)[1])

        return result

    def topKFrequentTiny(self, nums, k):
        counts = Counter(nums)
        heap = [(-c, item) for item, c in counts.items()]
        heapq.heapify(heap)  # O(m), instead of m pushes
        return [heapq.heappop(heap)[1] for _ in range(k)]

    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        # Counting: O(n)
        for num in nums:
            counts[num] += 1

        # Filling buckets: O(m)
        bucket_counts = [[] for _ in range(len(nums) + 1)] # + 1 because max counts can be the length, needs index shift
        for item, count in counts.items():
            bucket_counts[count].append(item)

        # Scanning buckets: O(n + m) = O(n)
        result = []
        for i in range(len(bucket_counts) - 1, 0, -1):
            for bucket_num in bucket_counts[i]:
                result.append(bucket_num)
                if len(result) == k:
                    return result

        return []


# Add each new variant's method name here (e.g. "topKFrequentHeap", "topKFrequentBucket").
METHODS = ["topKFrequent", "topKFrequentTiny", "topKFrequentBucketSort"]


# Answer can come back in any order, so compare sorted.
@pytest.mark.parametrize("method", METHODS)
def test_example_1(method):
    assert sorted(getattr(Solution(), method)([1, 2, 2, 3, 3, 3], 2)) == [2, 3]


@pytest.mark.parametrize("method", METHODS)
def test_example_2(method):
    assert sorted(getattr(Solution(), method)([7, 7], 1)) == [7]


@pytest.mark.parametrize("method", METHODS)
def test_k_equals_number_of_distinct(method):
    assert sorted(getattr(Solution(), method)([4, 1, 4, 2, 1, 4], 3)) == [1, 2, 4]


@pytest.mark.parametrize("method", METHODS)
def test_negative_numbers(method):
    assert sorted(getattr(Solution(), method)([-1, -1, -2, 3, 3, 3], 2)) == [-1, 3]


@pytest.mark.parametrize("method", METHODS)
def test_single_element(method):
    assert getattr(Solution(), method)([5], 1) == [5]
