from random import randint


class Solution:
    def sort(self, array):

        return self.quicksort(array, 0, len(array) - 1)

    def quicksort(self, array, start, end):
        if start >= end: return

        l, r = start, end
        pivot = array[randint(l, r)]

        while l < r:
            while array[l] < pivot: l += 1
            while array[r] > pivot: r -= 1

            if l <= r:
                array[l], array[r] = array[r], array[l]
                l += 1
                r -= 1

        self.quicksort(array, start, r)
        self.quicksort(array, l, end)


if __name__ == '__main__':
    a = [0, 5, 4, 7, 3, 5, 3, 2, 56]
    Solution().sort(a)
    print(a)
