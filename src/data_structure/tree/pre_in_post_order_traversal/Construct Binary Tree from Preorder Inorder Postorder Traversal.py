# Definition for a binary tree node.
from src.data_structure.tree.pre_in_post_order_traversal.tree_basic_traversal import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is
# the inorder traversal of the same tree, construct and return the binary tree.

class Solution105:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(in_left, in_right):  # O(n) time complexity since every node we only consider one time
            nonlocal pre_idx
            if in_left == in_right: return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            root.left = dfs(in_left, index)
            root.right = dfs(index + 1, in_right)
            return root

        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}  # space complexity O(n)
        return dfs(0, len(inorder))


# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and
# postorder is the postorder traversal of the same tree, construct and return the binary tree.
class Solution106:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index_map = {val: idx for idx, val in enumerate(inorder)}  # space complexity O(n)
        post_idx = -1

        def dfs(in_left, in_right):  # O(n) time complexity since every node we only consider one time
            nonlocal post_idx
            if in_left == in_right: return

            val = postorder[post_idx]
            root = TreeNode(val)

            idx = index_map[val]
            post_idx -= 1

            root.right = dfs(idx + 1, in_right)
            root.left = dfs(in_left, idx)

            return root

        return dfs(0, len(inorder))


# Return any binary tree that matches the given preorder and postorder traversals.
#
# Values in the traversals pre and post are distinct positive integers.
class Solution889:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def make(pre_left, post_left, N):  # O(N)
            if N == 0: return None
            root = TreeNode(pre[pre_left])
            if N == 1: return root

            L = idx[pre[pre_left + 1]] - post_left + 1

            root.left = make(pre_left + 1, post_left, L)
            root.right = make(pre_left + L + 1, post_left + L, N - 1 - L)
            return root

        idx = {v: i for i, v in enumerate(post)}  # O(N)
        return make(0, 0, len(pre))


if __name__ == '__main__':
    root = Solution105().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(preorder_traversal_recursion(root))  # [3,9,20,null,null,15,7]

    root = Solution106().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(preorder_traversal_recursion(root))  # [3,9,20,null,null,15,7]

    root = Solution889().constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    print(preorder_traversal_recursion(root))  # [3,9,20,null,null,15,7]
