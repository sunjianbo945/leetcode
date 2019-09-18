import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dict_t = collections.Counter(t)

        required = len(dict_t)

        l, r, dict_s = 0, 0, {}

        formed = 0
        res = s + '1'

        while r < len(s):

            if s[r] in dict_t:
                dict_s[s[r]] = dict_s.get(s[r], 0) + 1
                if dict_s[s[r]] == dict_t[s[r]]:
                    formed += 1

                while l <= r and formed == required:
                    res = s[l:r + 1] if r - l + 1 < len(res) else res

                    if s[l] in dict_s:
                        dict_s[s[l]] -= 1
                        if dict_s[s[l]] < dict_t[s[l]]:
                            formed -= 1
                    l += 1

                    if formed != required:
                        while l <= r and s[l] not in dict_s:
                            l += 1

            r += 1

        return res if len(res) <= len(s) else ''