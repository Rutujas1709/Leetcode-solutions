class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ' '
        prefix = strs[0]
 
        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix)-1]
            if not prefix:
                break
        res = prefix
        return res