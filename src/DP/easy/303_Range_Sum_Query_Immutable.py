
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.cul_sum = [sum(nums[:i + 1]) for i in range(len(nums))]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.cul_sum[j]
        return self.cul_sum[j] - self.cul_sum[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

def main():
    print(NumArray([-2, 0, 3, -5, 2, -1]).sumRange(0,4))


if __name__=='__main__':
    main()