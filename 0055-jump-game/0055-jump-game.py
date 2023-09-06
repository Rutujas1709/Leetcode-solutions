class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums) - 1
        # maxjump = 0
        # ins = nums[0]
        for i in range(len(nums))[::-1]:
    
            if i + nums[i] >= size:
                size = i
            
        return not size        
        