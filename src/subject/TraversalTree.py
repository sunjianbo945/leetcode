def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right


# An iterative process to print preorder traveral of BT
def iterativePreorder(root):
    # Base CAse
    if root is None:
        return

        # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    #  Pop all items one by one. Do following for every popped item
    #   a) print it
    #   b) push its right child
    #   c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while (len(nodeStack) > 0):

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print
        node.data,

        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

        # Iterative function for inorder tree traversal


def inorderTraversal(root):
    # Set current to root of binary tree
    current = root

    while current:

        if current.left is None:
            print(current.data)
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

                # Make current as right child of its inorder predecessor
            if not pre.right:
                pre.right = current
                current = current.left

                # Revert the changes made in if part to restore the
            # original tree i.e., fix the right child of predecessor
            else:
                pre.right = None
                print
                current.data,
                current = current.right


class newNode:
    # Constructor to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False

def postorder(head) :
    temp = head

    while temp and temp.visited == False:
        # Visited left subtree
        if temp.left and temp.left.visited == False:
            temp = temp.left
        # Visited right subtree
        elif temp.right and temp.right.visited == False:
            temp = temp.right
        # Print node
        else:
            print(temp.data, end = ' ')
            temp.visited = True
            temp = head

