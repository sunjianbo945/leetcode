from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        backup = {}

        self.dfs(s, wordDict, backup)
        return [bu[:-1] for bu in backup[s]]

    def dfs(self, s, wordDict, backup):
        if not s:
            return ['']
        if s not in backup:
            backup[s] = []
            for i in range(1, len(s) + 1):
                word = s[:i]
                if word in wordDict:
                    sentences = self.dfs(s[i:], wordDict, backup)
                    for ss in sentences:
                        backup[s].append(word + ' ' + ss)
        return backup[s]


def main():
    print(Solution().wordBreak("catsanddog",["cat","cats","and","sand","dog"]))


if __name__=='__main__':
    main()