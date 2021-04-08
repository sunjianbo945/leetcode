from collections import Counter, defaultdict
from typing import List


# https://leetcode.com/problems/valid-parentheses/
class Solution20:
    def isValid(self, s: str) -> bool:
        p_map = {')': '(', ']': '[', '}': '{'}

        stack = []
        for c in s:
            if c in p_map:
                if not stack: return False
                if stack[-1] != p_map[c]: return False
                stack.pop()
            else:
                stack.append(c)

        return not stack


# https://leetcode.com/problems/asteroid-collision/
class Solution735:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while ast < 0 and stack and stack[-1] > 0:
                if ast + stack[-1] < 0:
                    stack.pop()
                elif ast + stack[-1] == 0:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ast)

        return stack


# https://leetcode.com/problems/min-stack/
class MinStack155:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.min.append(x)
            return

        if x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])

        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution1047:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack:
                stack.append(c)
                continue

            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


# https://leetcode.com/problems/remove-duplicate-letters/
class Solution316:
    def removeDuplicateLetters(self, s: str) -> str:
        char_last_pos = {}
        for i, c in enumerate(s):
            char_last_pos[c] = i

        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c in seen: continue

            while stack and c < stack[-1] and char_last_pos[stack[-1]] > i:
                old = stack.pop()
                seen.remove(old)

            seen.add(c)
            stack.append(c)

        return ''.join(stack)


# https://leetcode.com/problems/score-of-parentheses/
class Solution856:
    def scoreOfParentheses(self, S):
        stack = [0]  # The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()


# https://leetcode.com/problems/maximum-frequency-stack/
class FreqStack895:

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f

        self.group[f].append(val)
        print(val, self.group)

    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x


# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue232:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2


# https://leetcode.com/problems/longest-valid-parentheses/
class Solution32:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()

                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)

        return res

    def longestValidParentheses_counter(self, s: str) -> int:
        l, r, max_len = 0, 0, 0

        for i, c in enumerate(s):
            if c == '(':
                l += 1
            else:
                r += 1

            if l == r:
                max_len = max(max_len, r * 2)

            if r > l:
                l, r = 0, 0

        l, r = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                l += 1
            else:
                r += 1

            if l == r:
                max_len = max(max_len, l * 2)

            if l > r:
                l, r = 0, 0

        return max_len