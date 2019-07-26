
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # reference https://www.cnblogs.com/grandyang/p/4257740.html

        dp = [False] * (len(s) + 1)  # dp[i] means the ith location s[:i+1] can work break
        dp[0] = True

        wordDict = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

def main():
    print(Solution().wordBreak("leetcode",["leet","code"]))


if __name__=='__main__':
    main()