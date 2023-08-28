class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        size = len(nums)
           
        for i in range(size):
            diff = target-nums[i]
            if diff in diff_dict:
                return [i, diff_dict[diff]]
            diff_dict[nums[i]] = i
