from typing import List


# https://leetcode.com/problems/can-place-flowers/
class Solution605:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cannot_plant = set()
        N = len(flowerbed)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i in cannot_plant: continue

                if i + 1 >= N or flowerbed[i + 1] != 1:
                    n -= 1

            cannot_plant.add(i)
            cannot_plant.add(i + 1)

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
