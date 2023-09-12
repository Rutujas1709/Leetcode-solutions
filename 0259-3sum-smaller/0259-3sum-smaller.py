

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the input list to make it easier to find triplets.
        n = len(nums)
        count = 0

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                if triplet_sum < target:
                    # If the sum is less than the target, all triplets in this range will also be less than the target.
                    # So, we increment the count by the number of triplets in this range (right - left).
                    count += right - left
                    left += 1  # Move the left pointer to the right to look for larger sums.
                else:
                    right -= 1  # If the sum is greater or equal to the target, decrease the right pointer.
        
        return count
