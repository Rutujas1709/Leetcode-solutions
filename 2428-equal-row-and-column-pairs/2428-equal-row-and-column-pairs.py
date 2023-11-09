class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                same = True

                for m in range(len(grid)):
                    if grid[i][m] != grid[m][j]:
                        same = False
                        break


                count += int(same)

        return count

            