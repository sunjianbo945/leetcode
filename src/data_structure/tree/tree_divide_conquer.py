from collections import *
from math import inf
from typing import *

from src.data_structure.tree.model import TreeNode


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


# https://leetcode.com/problems/most-frequent-subtree-sum/
class Solution508:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None: return []

        def dfs(node):
            if node is None: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        count = Counter()
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


# https://leetcode.com/problems/longest-univalue-path/
class Solution687:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = -inf

        def dfs(node):
            nonlocal res
            if not node: return None, 0

            l_val, l_count = dfs(node.left)
            r_val, r_count = dfs(node.right)

            if l_val == r_val == node.val:
                res = max(res, l_count + r_count + 1)
                return node.val, max(l_count, r_count) + 1
            elif l_val == node.val:
                res = max(res, l_count + 1)
                return node.val, l_count + 1
            elif r_val == node.val:
                res = max(res, r_count + 1)
                return node.val, r_count + 1
            else:
                return node.val, 1

        dfs(root)
        return res - 1 if res > -inf else 0


# https://leetcode.com/problems/delete-leaves-with-a-given-value/
class Solution1325:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def dfs(node):
            if not node: return False

            left = dfs(node.left)
            right = dfs(node.right)

            if left: node.left = None
            if right: node.right = None

            if node.val == target and not node.left and not node.right:
                return True

            return False

        dfs(root)
        if root.val == target and not root.left and not root.right: return None
        return root


# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
class Solution1315:
    def sumEvenGrandparent(self, root: TreeNode) -> int:  # this method is not generic.
        def dfs(node, p, gp):
            if not node: return 0
            res = node.val if gp % 2 == 0 else 0
            res += dfs(node.left, node.val, p)
            res += dfs(node.right, node.val, p)

            return res

        return dfs(root, 1, 1)

    def sumEvenGrandparent_right(self, root: TreeNode) -> int:  # this is better

        if not root: return 0

        res = 0
        if root.val % 2 == 0:
            grandChildren = self.getNodes(root, 2)
            for gc in grandChildren:
                res += gc.val

        return self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)

    def getNodes(self, node, depth) -> List['TreeNode']:
        if not node: return []
        if depth == 0: return [node]

        return self.getNodes(node.left, depth - 1) + self.getNodes(node.right, depth - 1)
