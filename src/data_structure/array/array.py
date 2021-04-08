from typing import List


# https://leetcode.com/problems/can-place-flowers/
class Solution605:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = list(flowerbed)
        N = len(bed)
        for i in range(N):
            if bed[i] == 0 and (i + 1 == N or bed[i + 1] != 1) and (i == 0 or bed[i - 1] != 1):
                bed[i] = 1
                n -= 1

        return n <= 0


# https://leetcode.com/problems/teemo-attacking/
class Solution495:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0

        res = 0
        n = len(timeSeries)
        for i in range(n - 1):
            diff = timeSeries[i + 1] - timeSeries[i]
            res += diff if diff < duration else duration

        return res + duration


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution122:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        res = 0
        for p in profit:
            res += max(0, p)

        return res


# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
class Solution1566:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        count = 0
        for i in range(len(arr) - m):
            count = count + 1 if arr[i] == arr[i + m] else 0

            if count == (k - 1) * m: return True

        return False