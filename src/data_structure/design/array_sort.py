# https://leetcode.com/problems/two-sum-iii-data-structure-design/
class TwoSum170:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.arr.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        self.arr.sort()
        l, r = 0, len(self.arr) - 1
        while l < r:
            curr = self.arr[l] + self.arr[r]
            if curr == value: return True

            if curr < value:
                l += 1
            else:
                r -= 1

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)