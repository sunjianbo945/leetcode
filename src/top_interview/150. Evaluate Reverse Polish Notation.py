from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operator = {'+', '-', '*', '/'}

        def operate(num1, num2, op):
            negative = False if int(num1)*int(num2)>0 else True
            if op == '+':
                return int(num1) + int(num2)
            elif op == '-':
                return int(num1) - int(num2)
            elif op == '*':
                return int(num1) * int(num2)
            else:
                n = abs(int(num1)) // abs(int(num2))
                return -1* n if negative else n

        def dfs(tokens, operator):

            if len(tokens) < 3:
                return int(tokens[-1])
            if len(tokens) == 3:
                return operate(tokens[0], tokens[1], tokens[2])

            for i in range(len(tokens)):
                if tokens[i] in operator:
                    num = operate(tokens[i - 2], tokens[i - 1], tokens[i])
                    return dfs(tokens[:i - 2] + [num] + tokens[i + 1:], operator)

        return dfs(tokens, operator)


if __name__ == '__main__':
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))