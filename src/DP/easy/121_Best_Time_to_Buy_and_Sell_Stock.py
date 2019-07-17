from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        num = 0
        max_num = prices[1] - prices[0]
        for i in range(0, len(prices) - 1):
            max_num = max(prices[i + 1] - prices[i] + num, max_num)
            num = max(0, prices[i + 1] - prices[i] + num)

        return max_num if max_num > 0 else 0


def main():
    print(Solution().maxProfit([2, 0, 3, 5, 2, 1]))


if __name__=='__main__':
    main()