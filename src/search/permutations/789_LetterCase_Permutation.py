from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        self.recur(S, '', ans)
        return ans

    def recur(self, S: str, cur: str, ans: List[str]) -> None:

        ans.append(cur + S)

        for index, value in enumerate(S):
            if value.isalpha():
                if value.isupper():
                    self.recur(S[index+1:], cur+S[:index]+value.lower(), ans)
                else:
                    self.recur(S[index+1:], cur+S[:index]+value.upper(), ans)


def main():
    print(Solution().letterCasePermutation('a1b2'))


if __name__=='__main__':
    main()