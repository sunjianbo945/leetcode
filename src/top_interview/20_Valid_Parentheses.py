class Solution:
    def isValid(self, s: str) -> bool:

        q = []
        m = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in '({[':
                q.append(char)
            elif char in ')}]':
                if not len(q):
                    return False

                old_char = q.pop()
                if old_char != m[char]:
                    return False
            else:
                continue

        return not len(q)
