# https://leetcode.com/problems/crawler-log-folder/
from typing import List


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


# https://leetcode.com/problems/simplify-path/
class Solution71:
    def simplifyPath(self, path: str) -> str:
        path_parts = path.split('/')
        stack = []
        for p in path_parts:
            if p == '' or p == '.': continue

            if p == '..':
                if stack:
                    stack.pop()
                continue

            stack.append(p)

        return '/' + '/'.join(stack)




# https://leetcode.com/problems/longest-absolute-file-path/
class Solution388:
    def lengthLongestPath(self, s: str) -> int:
        paths, stack, res = s.split('\n'), [], 0

        for path in paths:
            p = path.split('\t')
            depth, name = len(p) - 1, p[-1]

            l = len(name)
            while stack and stack[-1][1] >= depth:
                stack.pop()

            if not stack:
                stack.append((l, depth))
            else:
                stack.append((l + stack[-1][0], depth))

            if '.' in name:
                res = max(res, stack[-1][0] + stack[-1][1])

        return res