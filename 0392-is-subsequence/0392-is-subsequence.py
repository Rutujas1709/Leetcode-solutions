class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = len(s), len(t)

        p_left = p_right = 0
        while p_left < left and p_right < right:
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == left