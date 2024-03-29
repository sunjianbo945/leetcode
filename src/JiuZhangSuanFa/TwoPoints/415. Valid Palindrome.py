class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here

        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not (s[left].isnumeric() or s[left].isalpha()):
                left += 1

            while left < right and not (s[right].isnumeric() or s[right].isalpha()):
                right -= 1

            if s[left].upper() != s[right].upper():
                return False

            left += 1
            right -= 1

        return True