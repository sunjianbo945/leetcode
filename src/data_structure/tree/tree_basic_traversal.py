from typing import List
from src.data_structure.tree.model import TreeNode, Node


# pre, in, post, order is relative to root

# preorder traversal
#      2
#     / \
#    1   3
#   /\
#  4  5
# is root -> left -> right : 2, 1, 4, 5, 3
def preorder_traversal_recursion(root: 'TreeNode'):
    if not root: return
    res = []

    def dfs(node):
        if not node: return

        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


def preorder_traversal_iterative(root: 'TreeNode'):
    if not root: return
    stack = [root]  # need a stack
    res = []
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return res


def preorder_divide_conquer(node):
    if not node: return []

    res = [node.val]
    # divide
    left = preorder_divide_conquer(node.left)
    right = preorder_divide_conquer(node.right)
    # conquer
    res.extend(left)
    res.extend(right)

    return res  # [node.val, *preorder_divide_conquer(node.left), *preorder_divide_conquer(node.right)]


# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
class Solution589:
    def preorderNary_iterative(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])  # stack do not have extend, should use for-loop

        return output

    def preorderNary_divide_conquer(self, root: 'Node') -> List[int]:
        res = []
        if not root: return res
        res.append(root.val)
        for child in root.children:
            if child:
                res += self.preorderNary_divide_conquer(child)

        return res

    def preorderNary_recursion(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            if not node: return

            res.append(node.val)
            for child in node.children():
                dfs(child)

        dfs(root)
        return res


# inorder traversal
#      2
#     / \
#    1   3
#   /\
#  4  5
# is left -> root -> right : 4, 1, 5, 2, 3
def inorder_traversal_recursion(root: 'TreeNode'):
    if not root: return
    res = []

    def dfs(node):
        if not node: return
        dfs(node.left)

        res.append(node.val)

        dfs(node.right)

    dfs(root)
    return res


def inorder_traversal_iterative(root: 'TreeNode') -> List[int]:
    if not root: return []
    stack = []
    curr = root
    res = []

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        # now curr is None
        curr = stack.pop()
        res.append(curr.val)

        curr = curr.right

    return res


def inorder_divide_conquer(root):
    if not root: return []

    res = []
    res += inorder_divide_conquer(root.left)

    res.append(root.val)

    res += inorder_divide_conquer(root.right)
    return res


# postorder traversal
#      2
#     / \
#    1   3
#   /\
#  4  5
# is left -> right -> root : 4, 5, 1, 3, 2 .
def postorder_traversal_recursion(root: 'TreeNode') -> List[int]:
    if not root: return []
    res = []

    def dfs(node):
        if not node: return
        dfs(node.left)
        dfs(node.right)

        res.append(node.val)

    dfs(root)
    return res


def postorder_traversal_iterative(root: 'TreeNode') -> List[int]:
    if not root: return []
    stack, output = [root, ], []
    while stack:
        curr = stack.pop()
        output.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return output[::-1]


def postorder_traversal_iterative2(root: 'TreeNode') -> List[int]:
    if not root: return []
    stack = []
    curr = root
    res = []
    while stack or curr:
        # push nodes: right -> node -> left
        while curr:  # push 3, 2, 5, 1, 4
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left

        # print(f'stack={stack}')
        curr = stack.pop()

        # if the right subtree is not yet processed
        if stack and curr.right == stack[-1]:
            stack[-1] = curr
            curr = curr.right
        # if we're on the leftmost leaf
        else:
            res.append(curr.val)
            curr = None

    return res


def postorder_divide_conquer(node: 'TreeNode'):
    if not node: return []

    res = []
    res += postorder_divide_conquer(node.left)
    res += postorder_divide_conquer(node.right)
    res.append(node.val)
    return res


if __name__ == '__main__':
    root = TreeNode(2)
    root.left, root.right = TreeNode(1), TreeNode(3)
    root.left.left, root.left.right = TreeNode(4), TreeNode(5)

    print(f'preorder_traversal_recursion results: {preorder_traversal_recursion(root)}')
    print(f'preorder_traversal_iterative results {preorder_traversal_iterative(root)}')
    print(f'preorder_divide_conquer running {preorder_divide_conquer(root)}')

    print(f'inorder_traversal_recursion results: {inorder_traversal_recursion(root)}')
    print(f'inorder_traversal_iterative results: {inorder_traversal_iterative(root)}')
    print(f'inorder_divide_conqur results: {inorder_divide_conquer(root)}')

    print(f'postorder_traversal_recursion results: {postorder_traversal_recursion(root)}')
    print(f'postorder_traversal_iterative results: {postorder_traversal_iterative(root)}')
    print(f'postorder_traversal_iterative2 results: {postorder_traversal_iterative2(root)}')
    print(f'postorder_divide_conqur results: {postorder_divide_conquer(root)}')
