# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stackA = []
        stackB = []

        while headA:
            stackA.append(headA)
            headA = headA.next

        while headB:
            stackB.append(headB)
            headB = headB.next

        pre = None
        while stackA and stackB:

            nodeA = stackA.pop()
            nodeB = stackB.pop()
            # print(' a:{},b:{}'.format(nodeA,nodeB))
            if nodeA.val == nodeB.val:
                pre = nodeA
            else:
                return pre

        return pre

