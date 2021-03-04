from collections import defaultdict
from math import inf
from typing import List

from src.data_structure.tree.model import TreeNode


# https://leetcode.com/problems/two-sum/
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = defaultdict()

        for idx, num in enumerate(nums):
            if target - num in num_idx:
                return [num_idx[target - num], idx]
            else:
                num_idx[num] = idx


# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        pre_sum = set()
        stack = [root]

        while stack:
            curr = stack.pop()

            if k - curr.val in pre_sum: return True
            pre_sum.add(curr.val)

            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)

        return False


# https://leetcode.com/problems/two-sum-bsts/
class Solution1214:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, k: int) -> bool:
        nums = set()

        def collect(node):
            if not node: return
            nums.add(node.val)
            collect(node.left)
            collect(node.right)

        collect(root1)

        def dfs(node):
            if not node: return False

            return k - node.val in nums or dfs(node.left) or dfs(node.right)

        return dfs(root2)


# https://leetcode.com/problems/count-good-meals/
class Solution1711:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = [2 ** i for i in range(0, 22)]  # 22 means two 2 2**20 gets sum 2**21

        num_count = defaultdict(int)
        res = 0
        for food in deliciousness:
            for good in powers:
                res += num_count[good - food]

            num_count[food] += 1

        return res % (10 ** 9 + 7)


# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution560:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum_count = defaultdict(int)
        pre_sum_count[0] = 1
        pre_sum = 0
        res = 0
        for num in nums:
            pre_sum += num
            res += pre_sum_count[pre_sum - k]
            pre_sum_count[pre_sum] += 1

        return res


# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
class Solution325:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pre_sum_idx = defaultdict()
        pre_sum_idx[0] = -1
        pre_sum = 0
        res = 0
        for idx, num in enumerate(nums):
            pre_sum += num

            if pre_sum - k in pre_sum_idx:
                res = max(res, idx - pre_sum_idx[pre_sum - k])

            if pre_sum in pre_sum_idx: continue
            pre_sum_idx[pre_sum] = idx

        return res


# https://leetcode.com/problems/contiguous-array/
class Solution525:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_sum_idx = defaultdict()
        pre_sum_idx[0] = -1
        pre_sum = 0
        res = 0
        for idx, num in enumerate(nums):
            pre_sum += num if num else -1

            if pre_sum in pre_sum_idx:
                res = max(res, idx - pre_sum_idx[pre_sum])

            if pre_sum in pre_sum_idx: continue
            pre_sum_idx[pre_sum] = idx

        return res


# https://leetcode.com/problems/continuous-subarray-sum/
class Solution523:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum_idx = defaultdict()
        pre_sum_idx[0] = -1
        pre_sum = 0
        for idx, num in enumerate(nums):
            pre_sum += num
            if k != 0:
                pre_sum %= k

            if pre_sum in pre_sum_idx:
                if idx - pre_sum_idx[pre_sum] > 1:
                    return True
            else:
                pre_sum_idx[pre_sum] = idx

        return False


# https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution974:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        pre_sum_count = defaultdict(int)
        pre_sum_count[0] = 1
        pre_sum = 0
        res = 0
        for idx, a in enumerate(A):
            pre_sum += a
            pre_sum %= K

            res += pre_sum_count[pre_sum]
            pre_sum_count[pre_sum] += 1

        return res


# https://leetcode.com/problems/make-sum-divisible-by-p/
class Solution1590:
    def minSubarray(self, nums: List[int], p: int) -> int:
        pre_sum_idx = defaultdict()
        pre_sum_idx[0] = -1
        pre_sum = 0
        res = inf
        need = sum(nums) % p
        for idx, num in enumerate(nums):
            pre_sum += num
            pre_sum %= p
            pre_sum_idx[pre_sum] = idx

            if (pre_sum - need) % p in pre_sum_idx:
                res = min(res, idx - pre_sum_idx[(pre_sum - need) % p])

        return res if res < len(nums) else -1


# https://leetcode.com/problems/find-pivot-index/
class Solution724:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        n = len(nums)
        for i in range(n):
            left_sum += nums[i]
            if left_sum - nums[i] == total - left_sum:
                return i
        return -1
