class Solution:

    def __init__(self):
        self.one_to_twenty = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
                              8: 'Eight',
                              9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                              15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        self.tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
                     9: 'Ninety'}
        self.hundred = ['Hundred', 'Thousand', 'Million', 'Billion']
        self.nums = [100, 1000, 1000 * 1000, 1000 * 1000 * 1000]

    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        res = self.translate(num)

        return res[1:]

    def translate(self, n):

        if n == 0: return ''

        if n < 20: return ' ' + self.one_to_twenty[n]

        if n < 100: return ' ' + self.tens[n // 10] + self.translate(n % 10)

        for i in range(3, -1, -1):
            if n >= self.nums[i]:
                return self.translate(n // self.nums[i]) + ' ' + self.hundred[i] + self.translate(n % self.nums[i])








