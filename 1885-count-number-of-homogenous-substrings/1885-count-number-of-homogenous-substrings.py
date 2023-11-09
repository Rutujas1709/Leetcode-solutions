class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        mod = 10**9 + 7
        current_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_count += 1
            else:
                count = (count + (current_count * (current_count + 1) // 2)) % mod
                current_count = 1

        count = (count + (current_count * (current_count + 1) // 2)) % mod

        return count
