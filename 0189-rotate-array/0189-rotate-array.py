class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Ensure k is within the valid range
        
        # Create a copy of the original list
        original = nums[:]
        
        # Update elements in nums based on the rotation
        for i in range(n):
            nums[(i + k) % n] = original[i]
