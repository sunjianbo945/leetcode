from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Binary_Tree_Level_Order_Traversal_102:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        ret = []
        while len(q):
            size = len(q)
            arr = []
            for i in range(0, size):
                node = q.pop(0)
                arr.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            ret.append(arr)

        return ret

class Binary_Tree_Level_Order_Traversal_II_107:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        ret = []
        while len(q):
            size = len(q)
            arr = []
            for i in range(0,size):
                node = q.pop(0)
                arr.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            ret = [arr]+ret

        return ret


# Definition for a Node.

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class N_ary_Tree_Level_Order_Traversal_429:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        ret = []
        while len(q):
            size = len(q)
            arr = []
            for i in range(0, size):
                node = q.pop(0)
                arr.append(node.val)
                if node.children is not None:
                    q.extend(node.children)

            ret.append(arr)

        return ret


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Leaf_Similar_Trees_872:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1=[]
        self.find_leaves(root1,leaves1)
        leaves2=[]
        self.find_leaves(root2,leaves2)
        return leaves1==leaves2

    def find_leaves(self,root, leaves):
        if root is None:
            return

        if root.left is None and root.right is None:
            leaves.append(root.val)
            return

        self.find_leaves(root.left, leaves)
        self.find_leaves(root.right, leaves)

# [0,8,1,null,null,3,2,null,4,5,null,null,7,6]
class Vertical_Order_Traversal_Binary_Tree_987:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        memo={}
        self.dfs(root,0,0, memo)
        ret = []
        for k, v in sorted(memo.items(),key=lambda kv: kv[0] ):
            ans = []
            for a,b in sorted(v.items(), key=lambda l : l[0]):
                ans.extend(sorted(b))

            ret.append(ans)

        return ret

    def dfs(self, root, x, y, memo):

        if root is None:
            return
        if x in memo:
            if y in memo[x]:
                memo[x][y].append(root.val)
            else:
                memo[x][y] = [root.val]
        else:
            temp={}
            temp[y] = [root.val]
            memo[x] = temp

        self.dfs(root.left,x-1,y+1, memo)
        self.dfs(root.right,x+1,y+1,memo)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root1 = stringToTreeNode(line);
            line = next(lines)
            root2 = stringToTreeNode(line);

            ret = Vertical_Order_Traversal_Binary_Tree_987().verticalTraversal(root1)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()