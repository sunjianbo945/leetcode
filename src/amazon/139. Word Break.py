class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)

        return self.dfs(word_set, s, 0, {})

    def dfs(self, word_set, s, start, memo):

        if start >= len(s):
            return True

        if start in memo:
            return memo[start]

        for i in range(start, len(s)):

            if s[start:i + 1] in word_set and self.dfs(word_set, s, i + 1, memo):
                memo[start] = True
                return True

        memo[start] = False
        return False

