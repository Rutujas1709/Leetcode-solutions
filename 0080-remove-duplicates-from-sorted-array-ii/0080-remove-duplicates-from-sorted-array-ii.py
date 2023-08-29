# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         size = len(nums)
#         ins = 2
#         for i in range(2, size):
#             if nums[i] != nums[i - 2]:
#                 nums[ins] = nums[i]
#                 ins = ins + 1
#         return ins   




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2:
            return size  # If the array has 0 or 1 element, no duplicates to remove
        
        ins = 2  # Initialize ins to 2 since we're skipping the first two elements
        for i in range(2, size):
            if nums[i] != nums[ins - 2]:
                nums[ins] = nums[i]
                ins = ins + 1
        return ins

           