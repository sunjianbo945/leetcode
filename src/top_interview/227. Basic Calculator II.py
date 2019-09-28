class Solution:
    def calculate(self, s: str) -> int:
        s = trim(s)
        stack = []

        pre_op = "+"

        num = 0

        for i in range(len(s)):

            if s[i] == ' ':
                continue

            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if i == len(s) - 1 or s[i] in '+-*/':

                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-1 * num)
                elif pre_op == '*':
                    stack.append(num * stack.pop())
                else:
                    if stack[-1] < 0:
                        stack.append(int(stack.pop() / num))
                    else:
                        stack.append(stack.pop() // num)

                pre_op = s[i]
                num = 0

        return sum(stack)


def stringToString(input):
    import json

    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().calculate(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()