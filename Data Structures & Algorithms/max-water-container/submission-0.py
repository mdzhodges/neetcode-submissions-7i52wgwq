class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # no sorting needed, the area is gonna be min(heights[right], heights[left]) * (j-i)

        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            area = min(heights[right], heights[left]) * (right - left)
            if area > max_area:
                max_area = area
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return max_area