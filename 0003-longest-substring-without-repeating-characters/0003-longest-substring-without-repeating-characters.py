class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        output = 0
        left = 0
        right = 0

        while left < n and right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                output = max(output, right - left)
            else:
                seen.remove(s[left])
                left += 1

        return output
