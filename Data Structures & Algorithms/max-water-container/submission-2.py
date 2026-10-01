class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = (r - l) * min(heights[l], heights[r])

        while l < r:
            if heights[l] <= heights[r]:
                l += 1 
            else:
                r -= 1
            area = (r - l) * min(heights[l], heights[r])
            result = max(area, result)
    
        return result

#[4, 3, 2, 1, 4]