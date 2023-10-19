class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones_count = data.count(1)  # Count the number of 1s in the array
        if ones_count == 0:
            return 0

    # Initialize variables for the sliding window
        max_ones = 0
        window_ones = 0

        # Calculate the number of 1s in the first window of size ones_count
        for i in range(ones_count):
            if data[i] == 1:
                window_ones += 1
        max_ones = window_ones

        # Slide the window and keep track of the maximum number of 1s
        for i in range(ones_count, len(data)):
            if data[i] == 1:
                window_ones += 1
            if data[i - ones_count] == 1:
                window_ones -= 1
            max_ones = max(max_ones, window_ones)

        # Calculate the minimum number of swaps required
        return ones_count - max_ones