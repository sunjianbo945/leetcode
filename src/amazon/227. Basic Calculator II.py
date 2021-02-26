# Given a string s which represents an expression, evaluate this expression and return its value.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: s = "3+2*2"
# Output: 7
#
# Example 2:
#
# Input: s = " 3/2 "
# Output: 1
#
# Example 3:
#
# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        pre_op = '+'
        for char in s + "+":

            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-*/':
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                num = 0
                pre_op = char

        return sum(stack)


import re

operator_definition = {
    "+": lambda x, y: x + y,
    '-': lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x**y
}
operator_priority = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}


def eval_str_expr(str_expr: str):
    number_or_symbol = re.compile(r'(\d+|[^ 0-9])')
    tokens = re.findall(number_or_symbol, str_expr)
    print(tokens)
    expr_queue = _process_tokens(tokens)
    print(expr_queue)
    return _eval_postfix(expr_queue)


def _process_tokens(tokens):
    operator_stack = []  # save operator
    res = []
    for token in tokens:
        if token.isnumeric():
            res.append(token)
        elif token in operator_definition:  # operators
            while operator_stack and operator_stack[-1] in operator_definition and _same_or_higher_priority(operator_stack[-1], token):
                res.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            # t := stack.pop() <- walrus operator in python 3.8
            while operator_stack[-1] != '(':
                res.append(operator_stack.pop())
            operator_stack.pop()  # because it is (
    # else such as ' ' will be ignored
    while operator_stack:
        res.append(operator_stack.pop())

    return res


def _same_or_higher_priority(op1, op2):  # op1 is same or higher order than op2

    return operator_priority.get(op1) >= operator_priority.get(op2)


def _cal(op1, op2, op):
    return operator_definition.get(op)(op1, op2)


def _eval_postfix(postfix_queue):
    stack = []
    for item in postfix_queue:
        if item in operator_definition:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(_cal(op1, op2, item))
        else:
            stack.append(int(item))

    return stack[0]


print(eval_str_expr(" 3+5 / 2 +3/2+1+(12+3) /5"))
