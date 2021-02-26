import collections
from collections import *
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution543:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res, left + right)
            return max(left, right) + 1

        dfs(root)
        return res


# https://leetcode.com/problems/path-sum/
class Solution112:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False

        def dfs(node, preSum):
            if not node: return False

            if not node.left and not node.right:  # this is leaf
                return node.val + preSum == targetSum

            return dfs(node.left, preSum + node.val) or dfs(node.right, preSum + node.val)

        return dfs(root, 0)


# https://leetcode.com/problems/path-sum-ii/solution/
class Solution113:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []

        def dfs(node, ancestors, preSum):
            if not node: return

            if not node.left and not node.right and node.val + preSum == targetSum:
                res.append(ancestors + [node.val])

            dfs(node.left, ancestors + [node.val], preSum + node.val)
            dfs(node.right, ancestors + [node.val], preSum + node.val)

        dfs(root, [], 0)
        return res


# https://leetcode.com/problems/path-sum-iii/
class Solution437:
    def pathSum(self, root: TreeNode, target: int) -> int:
        res = 0
        cum_sum = Counter()  # cumulative sum and happend times
        cum_sum[0] = 1

        def dfs(node, prev_sum):
            nonlocal res
            if not node: return

            curr_sum = prev_sum + node.val
            res += cum_sum[curr_sum - target]
            cum_sum[curr_sum] += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            cum_sum[curr_sum] -= 1  # backtrack

        dfs(root, 0)
        return res


# https://leetcode.com/problems/sum-root-to-leaf-numbers/
class Solution129:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, prev_sum):
            nonlocal res
            if not node: return

            if not node.left and not node.right:
                res += prev_sum + node.val
                return

            next_sum = (prev_sum + node.val) * 10

            dfs(node.left, next_sum)
            dfs(node.right, next_sum)

        dfs(root, 0)
        return res


# https://leetcode.com/problems/path-sum-iv/
class Solution666:
    def pathSum(self, nums: List[int]) -> int:

        depth_pos_val = defaultdict(Counter)

        def parse(num):  # depth, pos, value
            return num // 100 - 1, num // 10 % 10 - 1, num % 10  # 113 -> 0, 0, 3

        def exist(depth, pos):  # similar to check the tree node exist
            return depth in depth_pos_val and pos in depth_pos_val[depth]

        for num in nums:  # build the tree using map
            depth, pos, val = parse(num)  # 113 -> 0, 0, 3
            depth_pos_val[depth][pos] = val

        res = 0

        def dfs(depth, pos, preSum):  # tree path sum
            nonlocal res
            if not exist(depth, pos): return

            curr = preSum + depth_pos_val[depth][pos]
            if not exist(depth + 1, 2 * pos) and not exist(depth + 1, 2 * pos + 1):  # leaf
                res += curr
                return

            dfs(depth + 1, 2 * pos, curr)
            dfs(depth + 1, 2 * pos + 1, curr)

        depth, pos, _ = parse(nums[0])
        dfs(depth, pos, 0)
        return res


# https://leetcode.com/problems/range-sum-of-bst/
class Solution938:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root: return 0
        count = 0
        if low <= root.val <= high:
            count = root.val

        return count + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
class Solution1339:
    def maxProduct(self, root: TreeNode) -> int:

        def tree_sum(node):  # total sum
            if not node: return 0
            left_sum = tree_sum(node.left)
            right_sum = tree_sum(node.right)

            return left_sum + right_sum + node.val

        best = 0

        def dfs(node):
            nonlocal best
            if not node: return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            product = total_sum * (tree_total_sum - total_sum)
            best = max(best, product)

            return total_sum

        tree_total_sum = tree_sum(root)
        dfs(root)
        return best % (10 ** 9 + 7)


# https://leetcode.com/problems/maximum-average-subtree/
class Solution1120:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        res = 0

        def dfs(node):
            nonlocal res
            if not node: return 0, 0

            leftTotal, leftCount = dfs(node.left)
            rightTotal, rightCount = dfs(node.right)

            total = leftTotal + rightTotal + node.val
            count = rightCount + leftCount + 1
            res = max(res, total / count)

            return total, count

        dfs(root)
        return res


# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
class Solution1026:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # each path maintain min, and max
        res = 0

        def dfs(node, minb, maxb):
            nonlocal res
            if not node:
                res = max(res, maxb - minb)
                return

            lb = min(minb, node.val)
            rb = max(maxb, node.val)

            dfs(node.left, lb, rb)
            dfs(node.right, lb, rb)

        dfs(root, float('inf'), float('-inf'))
        return res


# https://leetcode.com/problems/binary-tree-maximum-path-sum/
class Solution124:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        def dfs(node):  # return one max path sum
            nonlocal res
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            local_max = node.val + max(max(left, right), 0)

            res = max(res, local_max, node.val + left + right)
            return local_max

        dfs(root)
        return res


# https://leetcode.com/problems/equal-tree-partition/submissions/
class Solution663:
    def checkEqualTree(self, root: TreeNode) -> bool:
        seen = []  # use list here since summation can offset to 0, and it may appear multiple times, map is also fine

        def dfs(node):
            if not node: return 0
            total = dfs(node.left) + dfs(node.right) + node.val
            seen.append(total)
            return total

        total = dfs(root)
        seen.pop()  # need to pop for case 0, -1, 1
        return total / 2.0 in seen


# https://leetcode.com/problems/average-of-levels-in-binary-tree/
class Solution637:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        res = []
        queue = [root]

        while queue:
            size = len(queue)
            s, count = 0, 0
            for _ in range(size):
                node = queue.pop(0)
                s += node.val
                count += 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(s / count)

        return res


# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
class Solution1161:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        level = 1
        res = 1
        queue = [root]

        while queue:
            size = len(queue)
            s = 0
            for _ in range(size):
                node = queue.pop(0)
                s += node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if s > max_sum:
                max_sum = s
                res = level
            level += 1

        return res


# https://leetcode.com/problems/most-frequent-subtree-sum/
class Solution508:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None: return []

        def dfs(node):
            if node is None: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        count = collections.Counter()
        dfs(root)
        maxCount = max(count.values())
        return [s for s in count if count[s] == maxCount]


# https://leetcode.com/problems/distribute-coins-in-binary-tree/
class Solution979:  # this is not related to statistics but divide and conquer
    def distributeCoins(self, root):
        res = 0

        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res += abs(left) + abs(right)
            return root.val + left + right - 1

        dfs(root)
        return res
