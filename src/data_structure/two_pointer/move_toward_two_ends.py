from math import inf


# https://leetcode.com/problems/longest-palindromic-substring/
class Solution5:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_num = -inf
        res = ''
        for i in range(n):
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                if max_num < r - l + 1:
                    max_num = r - l + 1
                    res = s[l:r + 1]
                r += 1
                l -= 1

            l, r = i, i + 1
            while 0 <= l and r < n and s[l] == s[r]:
                if max_num < r - l + 1:
                    max_num = r - l + 1
                    res = s[l:r + 1]
                r += 1
                l -= 1

        return res


# https://leetcode.com/problems/valid-parenthesis-string/
class Solution678:
    def checkValidString(self, s: str) -> bool:
        bal_l = bal_r = 0
        for c in s:
            bal_l += 1 if c == '(' else -1
            bal_r += 1 if c != ')' else -1
            if bal_r < 0: break
            bal_l = max(bal_l, 0)

        return bal_l == 0