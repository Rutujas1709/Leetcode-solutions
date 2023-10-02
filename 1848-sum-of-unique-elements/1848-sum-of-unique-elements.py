class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        temp = []  # Initialize an empty list to store unique elements
        
        for i in nums:
            if nums.count(i) == 1:  # Check if the element appears only once
                temp.append(i)  # Add unique element to the list
        
        return sum(temp)  # Return the sum of unique elements

                


        