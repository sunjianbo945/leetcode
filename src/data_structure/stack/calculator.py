from typing import List


# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution150:
    def evalRPN(self, tokens: List[str]) -> int:
        df = {
            "+": lambda x, y: x + y,
            '-': lambda x, y: x - y,
            "*": lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        stack = []

        for token in tokens:
            if token in df:
                second = stack.pop()
                first = stack.pop()
                stack.append(df[token](first, second))
            else:
                stack.append(int(token))

        return stack.pop()


# https://leetcode.com/problems/baseball-game/
class Solution682:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for o in ops:
            if o == 'C':
                stack.pop()
            elif o == 'D':
                stack.append(stack[-1] * 2)
            elif o == '+':
                f = stack[-1]
                s = stack[-2]
                stack.append(f + s)
            else:
                stack.append(int(o))

        return sum(stack)


# https://leetcode.com/problems/backspace-string-compare/
class Solution844:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def operate(ops):
            stack = []
            for o in ops:
                if o == '#':
                    if not stack: continue

                    stack.pop()
                else:
                    stack.append(o)
            return stack

        return operate(S) == operate(T)


# https://leetcode.com/problems/crawler-log-folder/
class Solution1598:
    def minOperations(self, logs: List[str]) -> int:
        go_back = '../'
        do_nothing = './'
        stack = []
        for log in logs:
            if log == go_back:
                if not stack: continue

                stack.pop()
            elif log == do_nothing:
                continue
            else:
                stack.append(log)

        return len(stack)


# https://leetcode.com/problems/decode-string/
class Solution394:
    def decodeString(self, s: str) -> str:
        n = len(s)
        idx, num = 0, 0
        stack = []
        res = ''
        while idx < n:
            if s[idx].isalpha():
                res += s[idx]
            elif s[idx].isnumeric():
                num = 10 * num + int(s[idx])
            elif s[idx] == '[':
                stack.append(res)
                stack.append(num)
                res = ''
                num = 0
            elif s[idx] == ']':
                times = stack.pop()
                res *= times
                res = stack.pop() + res
                num = 0

            idx += 1

        return res