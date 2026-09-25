class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        # 平手的話收右邊
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            best = max(best, area)

            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1
        return best

# [1, 1]
# [4, 2, 1, 4]
