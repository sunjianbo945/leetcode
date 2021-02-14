from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.dfs(digit_map, digits, 0, '', res)
        return res

    def dfs(self, digit_map, digits, p, cur, res):
        '''
        digit_map: dictionary
        digits: like '23'
        p: poistion at digits
        cur: current list
        res: result list
        '''
        # position p at the end of the digits
        # boundary condition
        if p == len(digits):
            # dfs functionality
            res.append(cur)
            return

            # letters like 'ghi' for digit '4'
        letters = digit_map[digits[p]]
        # recursion
        for i in range(len(letters)):
            self.dfs(digit_map, digits, p + 1, cur + letters[i], res)
