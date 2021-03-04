# https://leetcode.com/problems/integer-to-english-words/
class Solution273:
    def numberToWords(self, num: int) -> str:
        one_digit = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }

        less_twenty = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }

        tens = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }

        hundreds = [100, 1000, 1000000, 1000000000]
        hundreds_str = ['Hundred', 'Thousand', 'Million', 'Billion']

        if num < 10: return one_digit[num]
        if num < 20: return less_twenty[num]

        for i in range(len(hundreds) - 1, -1, -1):
            q, r = divmod(num, hundreds[i])
            if q > 0 and r != 0:
                return '{} {} {}'.format(self.numberToWords(q), hundreds_str[i], self.numberToWords(r))
            elif q > 0 and r == 0:
                return '{} {}'.format(self.numberToWords(q), hundreds_str[i])

        # less than 100 and greater than 20
        if num % 10 == 0: return tens[num // 10]
        q, r = divmod(num, 10)
        return '{} {}'.format(tens[q], one_digit[r])


# https://leetcode.com/problems/integer-to-roman/
class Solution12:
    def intToRoman(self, num: int) -> str:
        roman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        res = ''

        for n, letter in roman.items():
            q, r = divmod(num, n)
            res += letter * q
            num = r
        else:
            return res


# https://leetcode.com/problems/roman-to-integer/
class Solution13:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total