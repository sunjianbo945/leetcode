from collections import *
from functools import *
from typing import *

from src.data_structure.tree.model import TreeNode, ListNode


# https://leetcode.com/problems/same-tree/
class Solution100:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not q or not p: return False

        return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def isSameTree_iterative(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]

        while stack:
            left, right = stack.pop()
            if not left and not right: continue
            if not left or not right: return False

            if left.val != right.val: return False

            stack.append((left.left, right.left))
            stack.append((left.right, right.right))

        return True


# https://leetcode.com/problems/symmetric-tree/
class Solution101:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if not left and not right: return True
            if not left or not right: return False

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

    def isSymmetric_iterative(self, root: TreeNode) -> bool:
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()
            if not left and not right: continue
            if not left or not right: return False

            if left.val != right.val: return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True


# https://leetcode.com/problems/subtree-of-another-tree/
class Solution572:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False

        def isSame(s, t):
            if not s and not t: return True
            if not s or not t: return False

            return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)

        return isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


# https://leetcode.com/problems/linked-list-in-binary-tree/
class Solution1367:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(head, root):
            if not head: return True
            if not root: return False

            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))

        if not head: return True
        if not root: return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# https://leetcode.com/problems/invert-binary-tree/
class Solution226:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return

        left = root.left
        right = root.right

        root.left = right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# https://leetcode.com/problems/merge-two-binary-trees/
class Solution617:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2: return
        if not root1: return root2
        if not root2: return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root

    def mergeTrees_iterative(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        stack = [(t1, t2)]
        while stack:
            curr1, curr2 = stack.pop()
            if not curr1 or not curr2: continue

            curr1.val += curr2.val
            if not curr1.left:
                curr1.left = curr2.left
            else:
                stack.append((curr1.left, curr2.left))

            if not curr1.right:
                curr1.right = curr2.right
            else:
                stack.append((curr1.right, curr2.right))
        return t1


# https://leetcode.com/problems/leaf-similar-trees/
class Solution872:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node: return []
            if not node.left and not node.right: return [node.val]

            return dfs(node.left) + dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


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


# https://leetcode.com/problems/binary-tree-paths/
class Solution257:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if not node: return

            path += str(node.val)
            if not node.left and not node.right:  # if reach a leaf
                paths.append(path)  # update paths
                return

            path += '->'  # extend the current path

            dfs(node.left, path)
            dfs(node.right, path)

        paths = []
        dfs(root, '')
        return paths


# https://leetcode.com/problems/path-sum-ii/
class Solution113:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []

        def dfs(node, ancestors, preSum):
            if not node: return

            if not node.left and not node.right and node.val + preSum == targetSum:
                res.append(ancestors + [node.val])
                return

            ancestors.append(node.val)
            dfs(node.left, ancestors, preSum + node.val)
            dfs(node.right, ancestors, preSum + node.val)
            ancestors.pop()  # backtrack

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


# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
class Solution671:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = float('inf')
        minimum = root.val

        def dfs(node):
            nonlocal res
            if not node: return

            if minimum < node.val < res:
                res = node.val
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res if res < float('inf') else -1


# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
class Solution1448:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, minimum):
            nonlocal count
            if not node: return

            if node.val >= minimum:
                count += 1
                minimum = node.val

            dfs(node.left, minimum)
            dfs(node.right, minimum)

        dfs(root, float('-inf'))
        return count


# https://leetcode.com/problems/delete-nodes-and-return-forest/
class Solution1110:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []

        def dfs(node, is_root):
            if not node: return None
            node_deleted = node.val in to_delete_set
            if is_root and not node_deleted: res.append(node)

            node.left = dfs(node.left, node_deleted)  # if the node get deleted, the child becomes root
            node.right = dfs(node.right, node_deleted)

            return None if node_deleted else node

        dfs(root, True)
        return res


# https://leetcode.com/problems/boundary-of-binary-tree/
class Solution545:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = [root.val]

        def left(node):
            if (not node) or (not node.left and not node.right): return
            print(node.val)
            res.append(node.val)
            if node.left:
                left(node.left)
            else:
                left(node.right)

        def right(node):
            if (not node) or (not node.left and not node.right): return
            if node.right:
                right(node.right)
            else:
                right(node.left)
            res.append(node.val)  # add reversal

        def leaves(node):
            if not node: return
            if not node.left and not node.right:
                res.append(node.val)
                return
            leaves(node.left)
            leaves(node.right)

        left(root.left)
        leaves(root.left)
        leaves(root.right)
        right(root.right)
        return res

    def boundaryOfBinaryTree_better(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res

        res.append(root.val)

        def dfs(node, lb, rb):  # lb, rb are booleans true when the node is left boundary or right boundary
            if not node: return
            if lb: res.append(node.val)  # append left boundary

            if not lb and not rb and not node.left and not node.right: res.append(node.val)  # leaves

            #     1
            #   /  \
            # 2      3
            #  \    /
            #   4  5
            dfs(node.left, lb, rb and not node.right)  # if node is on right branch, lb never been true
            dfs(node.right, lb and not node.left, rb)

            if rb: res.append(node.val)  # append right boundary

        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return res


# https://leetcode.com/problems/binary-tree-pruning/
class Solution814:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0: node.left = None
            if right == 0: node.right = None

            return node.val + left + right

        number = dfs(root)
        return None if number == 0 and root.val == 0 else root


# https://leetcode.com/problems/binary-tree-upside-down/
class Solution156:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root: return None

        def dfs(node):
            if not node: return
            if not node.left and not node.right: return node

            root = dfs(node.left)  # only left

            left = node.left
            right = node.right

            left.right = node
            left.left = right

            node.left = None  # must reset left and right
            node.right = None

            return root

        return dfs(root)


# https://leetcode.com/problems/unique-binary-search-trees/
# https://leetcode.com/problems/unique-binary-search-trees-ii/
class Solution95:
    def generateTrees(self, n: int) -> List[TreeNode]:
        @lru_cache(None)
        def dfs(start, end):
            if start > end: return [None]

            res = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left = dfs(start, i - 1)
                # all possible right subtrees if i is choosen to be a root
                right = dfs(i + 1, end)
                # connect left and right subtrees to the root i
                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        res.append(curr)

            return res

        return dfs(1, n) if n else []

    def numTrees(self, n: int) -> int:  # this is dp not tree
        # 区间型动态规划，都是dp[i][j]
        # 由小的区间先计算，然后计算大的区间得到，模板就是：
        # for len in range(2, n + 1):
        #     for i in range(0, n - len + 1):
        #         j = i + len - 1

        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for l in range(2, n + 1):
            for i in range(1, l + 1):
                dp[l] += dp[i - 1] * dp[l - i]

        return dp[n]


# https://leetcode.com/problems/all-possible-full-binary-trees/
class Solution894:
    def allPossibleFBT(self, N):
        @lru_cache(None)
        def dfs(N):
            if N == 1: return [TreeNode(0)]  # base case

            res = []
            for i in range(N):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left = dfs(i)
                # all possible right subtrees if i is choosen to be a root
                right = dfs(N - 1 - i)
                # connect left and right subtrees to the root i
                for l in left:
                    for r in right:
                        curr = TreeNode(0)
                        curr.left = l
                        curr.right = r
                        res.append(curr)

            return res

        return dfs(N) if N else []


# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
class Solution1379:
    def getTargetCopy_recursion(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o: TreeNode, c: TreeNode):
            if not o: return
            inorder(o.left, c.left)
            if o is target:
                self.ans = c
                return
            inorder(o.right, c.right)

        inorder(original, cloned)
        return self.ans

    def getTargetCopy_iterative(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack_o, stack_c = [], []
        node_o, node_c = original, cloned

        while stack_o or node_c:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)

                node_o = node_o.left
                node_c = node_c.left

            node_o = stack_o.pop()
            node_c = stack_c.pop()

            if node_o is target:
                return node_c

            node_o = node_o.right
            node_c = node_c.right

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue_o = deque([original, ])
        queue_c = deque([cloned, ])

        while queue_o:
            node_o = queue_o.popleft()
            node_c = queue_c.popleft()

            if node_o is target:
                return node_c

            if node_o:
                queue_o.append(node_o.left)
                queue_o.append(node_o.right)

                queue_c.append(node_c.left)
                queue_c.append(node_c.right)


'''
FaceBook interview:
Given a binary tree, with integer values at each node(Each node must have a value between 0-9 inclusive). Please return 
the sum of the numbers represented by the values on each node in each root-to-leaf path. The level of the tree is the
 significance digit on the number. Please see the example below
 root => 2
        / \
       3   4
     /  \
    1    5
The output should be: 231 + 235 + 24 = 490
'''


def func(root):
    res = 0

    def dfs(node, pre):
        nonlocal res
        if not node: return

        curr = pre * 10 + node.val
        if not node.left and not node.right:
            res += curr
            return

        dfs(node.left, curr)
        dfs(node.right, curr)

    dfs(root, 0)
    return res
