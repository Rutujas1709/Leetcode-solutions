class Solution:
    def isHappy(self, n: int) -> bool:

        def cal_power_sum(n):
            total = 0
            while n > 0:
                n, remainder = divmod(n, 10)
                total += remainder ** 2
            return total

        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = cal_power_sum(n)

        return n == 1
