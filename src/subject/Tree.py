class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left =None
        self.right = None


class Tree:

    def __init__(self):
        pass

    def pre_order_traverse(self,root):

        if not root:return []

        res = []

        def dfs(node,res):
            if not node:return

            res.append(node.val)
            dfs(node.left,res)
            dfs(node.right,res)

        dfs(root,res)
        return res


    def pre_order_iterative(self, root):

        if not root:return []

        stack = [root]

        res =[]

        while stack:

            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

    def pre_order_divide_conquer(self,node):

        if not node:return []

        res=[node.val]
        left = self.pre_order_divide_conquer(node.left)
        right = self.pre_order_divide_conquer(node.right)
        res.extend(left)
        res.extend(right)

        return res

    def in_order_traverse(self,root):
        if not root:return []

        res = []
        def dfs(node,res):

            if not node:return

            dfs(node.left,res)
            res.append(node.val)
            dfs(node.right,res)

        dfs(root,res)
        return res


    def in_order_iterative(self,root):

        if not root:return []

        stack = []
        res = []
        cur  = root
        while stack or cur:

            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.val)
                cur = node.right

        return res

    def in_order_divide_conqur(self,root):

        if not root:return []

        res =[]
        left = self.in_order_divide_conqur(root.left)
        res += left
        res.append(root.val)
        right = self.in_order_divide_conqur(root.right)
        res+=right
        return res

    def post_order_traverse(self,root):
        if not root:return []
        def dfs(node,res):
            if not node:return

            dfs(node.left,res)
            dfs(node.right,res)
            res.append(node.val)

        res=[]
        dfs(root,res)
        return res


    def post_order_divide_conqur(self,node):

        if not node:return []

        res = []
        left = self.post_order_divide_conqur(node.left)
        right = self.post_order_divide_conqur(node.right)
        res+=left
        res+=right
        res.append(node.val)
        return res



def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # print(Tree().pre_order_traverse(root))
    # print(Tree().pre_order_iterative(root))
    # print(Tree().pre_order_divide_conquer(root))

    # print(Tree().in_order_traverse(root))
    # print(Tree().in_order_iterative(root))
    # print(Tree().in_order_divide_conqur(root))

    print(Tree().post_order_traverse(root))
    print(Tree().post_order_divide_conqur(root))






if __name__ == '__main__':
    main()