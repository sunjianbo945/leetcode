from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Sum_Root_to_Leaf_Numbers_129:
    def sumNumbers(self, root: TreeNode) -> int:
        ret = []
        self.helper(root,'',ret)

        return sum(ret)

    def helper(self,node:TreeNode, s:str,ret:List[int]):

        if not node:
            return

        if not node.left and not node.right:
            ret.append(int(s+str(node.val)))

        self.helper(node.left,s+str(node.val),ret)
        self.helper(node.right,s+str(node.val),ret)



class Binary_Tree_Paths_257:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []
        self.helper(root, '', ret)
        return ret

    def helper(self, node: TreeNode, s: str, ret: List[str]):

        if not node:
            return

        if not node.left and not node.right:
            ret.append('{}->{}'.format(s,node.val)[2:])

        self.helper(node.left, '{}->{}'.format(s,node.val), ret)
        self.helper(node.right, '{}->{}'.format(s,node.val), ret)