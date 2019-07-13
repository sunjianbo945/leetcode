# leetcode link
# Difficulty: **
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# DFS & BFS

from typing import List


class Solution:

#region DFS

    def letter_combinations_dfs(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        combinations = []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        self.dfs_helper(phone, digits, "", combinations)

        return combinations

    def dfs_helper(self, phone_book, digits, cur, result):

        if len(digits) == 0:
            result.append(cur)
            return

        digit = digits[0]

        word = phone_book[digit]

        for i in range(len(word)):
            self.dfs_helper(phone_book, digits[1:], cur + word[i], result)

#endregion

#region BFS
    def letter_combinations_bfs(self,digits:str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return []

        combinations = [""]

        for digit_index in range(len(digits)):
            temp = []
            digit = digits[digit_index]
            for i in range(len(combinations)):
                for j in range( len(phone[digit])):
                    temp.append(combinations[i]+phone[digit][j])

            combinations = temp
        return combinations

#endregion
    def letter_combinations(self, digits:str) -> List[str]:
        temp = self.letter_combinations_dfs(digits)
        temp = self.letter_combinations_bfs(digits)
        return temp



def main():
    print(Solution().letter_combinations('23'))


if __name__ == '__main__':
    main()
