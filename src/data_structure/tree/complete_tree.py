from collections import defaultdict, Counter, deque
from typing import List

from src.data_structure.tree.model import TreeNode


# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
class Solution958:
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        seq = 1
        while nodes:
            node, v = nodes.pop(0)

            if seq != v: return False
            seq += 1

            if node.left: nodes.append((node.left, 2 * v))
            if node.right: nodes.append((node.right, 2 * v + 1))

        return True


# https://leetcode.com/problems/maximum-width-of-binary-tree/
class Solution662:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        # queue of elements [(node, col_index)]
        queue = deque()
        queue.append((root, 0))

        while queue:
            size = len(queue)
            _, most_left = queue[0]
            mark = most_left
            for _ in range(size):
                node, mark = queue.popleft()
                # preparing for the next level
                if node.left: queue.append((node.left, 2 * mark))
                if node.right: queue.append((node.right, 2 * mark + 1))

            res = max(res, mark - most_left + 1)

        return res


# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
class Solution1104:
    def pathInZigZagTree(self, label: int) -> List[int]:  # O(d)
        level, tot = -1, 0
        while label > tot:
            level += 1
            tot += (2 ** level)

        level -= 1
        cur = label // 2
        res = [label]
        while level > -1:
            st, end = 2 ** level, (2 ** (level + 1)) - 1
            cur = st + end - cur  # the reason this work since two node from most left + most right are switched
            res.append(cur)
            level -= 1
            cur = cur // 2
        return res[::-1]


# https://leetcode.com/problems/count-complete-tree-nodes/
class Solution222:
    def countNodes(self, root: TreeNode) -> int:  # O (logn*logn)
        ## RC ##
        ## APPROACH : RECURSION ##
        ## TIME COMPLEXICITY : LOG N * LOG N ##

        ## LOGIC ##
        # If left sub tree height equals right sub tree height then,
        #       a. left sub tree is perfect binary tree
        #       b. right sub tree is complete binary tree
        # If left sub tree height greater than right sub tree height then,
        #       a. left sub tree is complete binary tree
        #       b. right sub tree is perfect binary tree

        if not root:
            return 0

        def depthLeft(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def depthRight(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d

        ld = depthLeft(root.left)
        rd = depthRight(root.right)

        if ld == rd:
            return 2 ** (ld + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


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
