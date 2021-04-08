from functools import lru_cache
from random import choice
from typing import *

from numpy import std, mean


class Pointer:
    def __init__(self, index, direction):
        self.index = index
        self.direction = direction


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        s, f = Pointer(0, 'r'), Pointer(0, 'r')
        pre = Pointer(0, 'r')
        s = self.getNext(nums, s)
        f = self.getNext(nums, f)
        f = self.getNext(nums, f)

        while s.index != f.index:
            if pre and s.index == pre.index: return False

            pre = s

            s = self.getNext(nums, s)
            f = self.getNext(nums, f)
            f = self.getNext(nums, f)

        return s.direction == f.direction

    def getNext(self, nums, pointer):

        num = nums[pointer.index]
        direction = 'r' if num > 0 else 'l'
        index = (num + pointer.index) % len(nums)

        return Pointer(index, direction)


Solution().circularArrayLoop([-2, 1, -1, -2, -2])

import re

number_or_symbol = re.compile(r'(\d+|[^ 0-9])')

str = "(1+2)*3"


def eval_str_expr(str_expr: str):
    tokens = re.findall(number_or_symbol, str_expr)
    print(tokens)
    expr_queue = _process_tokens(tokens)
    return _eval_postfix(expr_queue)


def _process_tokens(tokens):
    print(tokens)
    operator = []  # save operator
    res = []  # save numbers
    for token in tokens:
        if token.isnumeric():
            res.append(token)

        elif token in '+-*/^(':  # operators
            while operator and operator[-1] in operator_definition and _same_or_higher_priority(operator[-1], token):
                res.append(operator.pop())
            operator.append(token)

        elif token == ')':
            while operator[-1] != '(':
                res.append(operator.pop())
            operator.pop()
    # else such as ' ' will be ignored
    while operator:
        res.append(operator.pop())

    return res


def _same_or_higher_priority(op1, op2):  # op1 is same or higher order than op2
    if op2 in '+-':
        return True
    elif op2 in '*/':
        return op1 in '*/^'
    else:
        return op1 == '^'


operator_definition = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}


def _eval_postfix(postfix_queue):
    print(postfix_queue)
    operand_stack = []
    while postfix_queue:
        item = postfix_queue.pop(0)
        if item.isnumeric():
            operand_stack.append(int(item))
        else:
            second = operand_stack.pop()
            first = operand_stack.pop()
            operand_stack.append(operator_definition[item](first, second))

    return operand_stack.pop()


# print(eval_str_expr('(81 * 6) / 42 + (3 - 1)'))
print(eval_str_expr('(81 + 6) / 42 + (3 - 1)'))
print(eval('(81 + 6) / 42 + (3 - 1)'))

# print(eval_str_expr('3+2*2'))
# print(eval_str_expr('3-(2-(1+2))'))
# print(eval_str_expr('3+2*2'))
# print(eval_str_expr('3*(2+2)'))


print(std([1, 2, 3, 4, 5, 6]))
print(mean([1, 2, 3, 4, 5, 6]))


def calculate():
    count = 0
    total = 1000
    idx = 0
    num = [1, 2, 3, 4, 5, 6]
    num2 = [0, 1]
    while idx < total:

        sum1 = sum([choice(num) for _ in range(10000)])
        sum2 = sum([choice(num2) for _ in range(60000)])
        if sum1 > sum2:
            count += 1
        else:
            print(sum1, sum2)

        idx += 1

    print(count / total)


calculate()


def fib(x):

    @lru_cache(None)
    def dfs(num):
        if num <= 1: return 1
        return dfs(num - 1) + dfs(num - 2)

    # x = 100
    # dfs(99) + dfs(98)
    # dfs(99) = dfs(98) + dfs(97)
    # dfs(4) = dfs(3) + dfs(2)
    # dfs(3) = dfs(2) + dfs(1)
    # dfs(2) = dfs(1) + dfs(0)
    return dfs(x)
