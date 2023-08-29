class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        ins = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[ins] = nums[i]
                ins = ins + 1
        return ins        
           
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         size = len(nums)
#         left = 1
#         for i in range(1, size):
#             if nums[i - 1] != nums[i]: 
#                 nums[left] = nums[i] 
#                 left = left + 1       
#         return left           
