class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, s, offset):
        # write your code here
        if not s: return s
        offset = offset % len(s)
        if offset == 0: return
        self.reverse(s, 0, len(s) - 1)
        self.reverse(s, 0, offset - 1)
        self.reverse(s, offset, len(s) - 1)

    def reverse(self, s, start, end):

        if start >= end:
            return

        while start < end:
            s[start], s[end] = s[end], s[start]

            start += 1
            end -= 1