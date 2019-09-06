from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Path_Sum_112:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return 0
        return self.recur_sum(root, 0, sum)

    def recur_sum(self, node, cur:int, sum:int):

        if node is None:
            return False

        if node.left is None and node.right is None:
            return cur+node.val==sum

        return self.recur_sum(node.left,cur+node.val,sum) or self.recur_sum(node.right, cur+node.val, sum)


class Path_Sum_II_113:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ret =[]
        self.recur_sum(root,[],0,sum,ret)
        return ret

    def recur_sum(self, node: TreeNode, path:List[int], cur:int, sum:int, ret:List[List[int]]):
        if not node:
            return

        if not node.left and not node.right and cur+node.val == sum:
                ret.append(path+[node.val])

        self.recur_sum(node.left, path+[node.val], cur+node.val, sum, ret)
        self.recur_sum(node.right,path+[node.val], cur+node.val, sum, ret)



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
            root = stringToTreeNode(line);
            line = next(lines)
            sum = int(line);

            ret = Solution().hasPathSum(root, sum)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()