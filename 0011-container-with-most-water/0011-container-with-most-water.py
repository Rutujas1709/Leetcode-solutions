class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        capacity = 0
        while left < right:

            breadth = min(height[left], height[right])
            width = right - left
            capacity = max(capacity, width*breadth)
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return capacity
