from collections import Counter
from typing import List


# https://leetcode.com/problems/exclusive-time-of-functions/
class Solution636:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        id_time = Counter()
        for log in logs:
            p_id, trans, time = log.split(':')
            time = int(time)
            if 'start' == trans:
                if stack:  # partial end for the previous process
                    id_time[stack[-1][0]] += time - stack[-1][1]

                stack.append([p_id, time])
            else:
                _, prev_time = stack.pop()
                id_time[p_id] += time - prev_time + 1

                if stack:  # partial start for the previous process
                    stack[-1][1] = time + 1

            # print(stack, id_time)
        return [id_time[str(i)] for i in range(n)]


# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution1209:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append((c, 1))
                continue

            if c != stack[-1][0]:
                stack.append((c, 1))
            else:
                _, count = stack.pop()
                stack.append((c, count + 1))

            while stack and stack[-1][1] == k:
                stack.pop()

        res = ''
        for char, count in stack:
            res += char * count

        return res
