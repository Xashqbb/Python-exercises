class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current_area is greater
            max_area = max(max_area, current_area)
            # Move the pointer for the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area