class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''

        memo = [[False] * len(s) for _ in range(len(s))]
        max_num = 1
        res = s[0]

        for i in range(len(s)):
            memo[i][i] = True

            if i + 1 < len(s):
                memo[i][i + 1] = s[i] == s[i + 1]

                if memo[i][i + 1] and max_num < 2:
                    max_num = 2
                    res = s[i:i + 2]

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, i + 1, -1):
                memo[i][j] = s[i] == s[j] and memo[i + 1][j - 1]
                if memo[i][j] and j - i + 1 > max_num:
                    max_num = j - i + 1
                    res = s[i:j + 1]

        return res

    def longestPalindrome1(self, s: str) -> str:
        if not s: return ''

        res = s[0]

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                l, r = i - 1, i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res = s[l:r + 1] if r - l + 1 > len(res) else res
                    l -= 1
                    r += 1

            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r + 1] if r - l + 1 > len(res) else res
                l -= 1
                r += 1
        return res



