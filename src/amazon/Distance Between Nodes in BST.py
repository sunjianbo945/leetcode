#
# Given a list of unique integers nums, construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two nodes node1 and node2. Distance is the number of edges between two nodes. If any of the given nodes does not appear in the BST, return -1.
#
# Example 1:
#
# Input: nums = [2, 1, 3], node1 = 1, node2 = 3
# Output: 2
# Explanation:
#      2
#    /   \
#   1     3

class Node:
    def __init__(self,val):
        self.val = val
        self.left=None
        self.right = None

def build_bst(array):

    def insert_tree(root,val):

        if not root:
            return Node(val)

        if root.val>val:
            root.right = insert_tree(root.right,val)
        else:
            root.left = insert_tree(root.left,val)

    root = Node(array[0])
    for i in range(1,len(array)):
        insert_tree(root,array[i])

    return root



def lca(root,node1,node2):

    if not root:return None

    if root.val == node1.val or root.val==node2.val:
        return root

    left = lca(root.left,node1,node2)
    right = lca(root.right,node1,node2)

    if left and right:
        return root

    return left if left else right


def find(line,val1,val2):
    node1= Node(val1)
    node2 = Node(val2)
    root = build_bst(line)
    common = lca(root,node1,node2)

    return getDis(common,node1) + getDis(common,node2)

def getDis(node1,node2):

    if not node1:return -1

    if node1.val == node2.val:
        return 0

    left = getDis(node1.left,node2)
    right = getDis(node1.right, node2)

    if left!=-1:
        return left+1

    if right!=-1:
        return right+1

    return -1

print(find([2, 1, 3],2,3))















