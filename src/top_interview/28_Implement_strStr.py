class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        s = len(needle)

        for i in range(len(haystack) - s + 1):

            if haystack[i:i + s] == needle:
                return i

        return -1
