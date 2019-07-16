
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        map = {}
        self.get(sorted(nums), target, map)

        return map.get(target)

    def get(self, nums: List[int], target: int, map) -> int:

        if target in map:
            return map.get(target)

        if target == 0:
            return 1

        # target does not in target. get it
        total = 0
        for i in range(len(nums)):
            if nums[i] > target:
                break
            total += self.get(nums, target - nums[i], map)

        map[target] = total
        return map.get(target)



def main():
    print(Solution().combinationSum4([10,1,2,7,6,1,5],8))

if __name__=='__main__':
    main()
