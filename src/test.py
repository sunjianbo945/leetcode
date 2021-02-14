from typing import *


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

import queue
import re

number_or_symbol = re.compile(r'(\d+|[^ 0-9])')

str = "(1+2)*3)"


def eval_str_expr(str_expr: str):
    tokens = re.findall(number_or_symbol, str_expr)
    print(tokens)
    expr_queue = _process_tokens(tokens)
    print(tokens)
    return _eval_postfix(expr_queue)


def _process_tokens(tokens):
    stack = [] # save operator
    output_queue = queue.Queue() # save numbers
    for token in tokens:
        if token.isnumeric():
            output_queue.put(token)
        elif token in '+-*/^':  # operators
            while stack and stack[-1] in '+-*/^' and _same_or_higher_priority(stack[-1], token):
                output_queue.put(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            # t := stack.pop() <- walrus operator in python 3.8
            while stack[-1] != '(':
                output_queue.put(stack.pop())
    # else such as ' ' will be ignored
    while stack:
        output_queue.put(stack.pop())

    return output_queue


def _same_or_higher_priority(op1, op2):  # op1 is same or higher order than op2
    if op2 in '+-':
        return True
    elif op2 in '*/':
        return op1 in '*/^'
    else:
        return op1 == '^'


def _eval_postfix(postfix_queue):
    operand_stack = []
    while not postfix_queue.empty():
        item = postfix_queue.get()
        if item.isnumeric():
            operand_stack.append(int(item))
        elif item in '+-*/^':
            first = operand_stack.pop()
            second = operand_stack.pop()

            if item == '+':
                operand_stack.append(second + first)
            elif item == '-':
                operand_stack.append(second - first)
            elif item == '*':
                operand_stack.append(second * first)
            elif item == '/':
                operand_stack.append(second / first)
            elif item == '^':
                operand_stack.append(second ** first)

    return operand_stack.pop()


# print(eval_str_expr('(81 * 6) / 42 + (3 - 1)'))
# print(eval('(81 * 6) / 42 + (3 - 1)'))
# print(eval_str_expr('3+2*2'))
# print(eval_str_expr('3-(2-(1+2))'))
# print(eval_str_expr('3+2*2'))
print(eval_str_expr('3*(2+2)'))
