from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            width = (r - l)  # distance between two pillars
            height = min(heights[l], heights[r])  # need to pick min since otherwise the water would leak
            max_area = max(max_area, (width * height))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

    def maxAreaBruteForce(self, heights: List[int]) -> int:
        max_area = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                width = (r - l)
                area = width * min(heights[l], heights[r])
                max_area = max(max_area, area)

        return max_area


heights = [1, 7, 2, 5, 4, 7, 3, 6]
print(Solution().maxArea(heights))
