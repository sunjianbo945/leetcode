from typing import List

from src.data_structure.linkedList.model import ListNode


# https://leetcode.com/problems/add-strings/
class Solution415:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1) - 1, len(num2) - 1
        if m < n: return self.addStrings(num2, num1)
        carry = 0
        res = []
        while m >= 0 or n >= 0:
            number1 = ord(num1[m]) - ord('0') if m >= 0 else 0
            number2 = ord(num2[n]) - ord('0') if n >= 0 else 0
            carry, value = divmod(number1 + number2 + carry, 10)
            res.append(value)
            m -= 1
            n -= 1

        if carry:
            res.append(carry)

        return ''.join(map(str, reversed(res)))


# https://leetcode.com/problems/add-to-array-form-of-integer/
class Solution989:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B = list(str(K))
        m, n, carry = len(A) - 1, len(B) - 1, 0
        res = []
        while m >= 0 or n >= 0:
            a = A[m] if m >= 0 else 0
            b = ord(B[n]) - ord('0') if n >= 0 else 0
            carry, value = divmod(a + b + carry, 10)
            res.append(value)
            m -= 1
            n -= 1

        if carry: res.append(carry)

        return res[::-1]


# https://leetcode.com/problems/plus-one/
class Solution66:
    def plusOne(self, digits: List[int]) -> List[int]:
        n, carry = len(digits) - 1, 1
        res = []
        while n >= 0:
            carry, value = divmod(digits[n] + carry, 10)
            res.append(value)
            n -= 1

        if carry: res.append(carry)
        return res[::-1]


# https://leetcode.com/problems/add-two-numbers/
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0

        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            carry, value = divmod(n1 + n2 + carry, 10)
            curr.next = ListNode(value)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry: curr.next = ListNode(carry)
        return dummy.next


# https://leetcode.com/problems/add-two-numbers-ii/
class Solution445:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next

        while l2:
            stack2.append(l2)
            l2 = l2.next

        carry = 0
        curr = None
        while stack1 or stack2:
            n1 = stack1.pop().val if stack1 else 0
            n2 = stack2.pop().val if stack2 else 0
            carry, val = divmod(n1 + n2 + carry, 10)

            curr = ListNode(val, curr)

        if carry:
            curr = ListNode(carry, curr)
        return curr


# https://leetcode.com/problems/merge-sorted-array/
class Solution88:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[last] = nums2[n]
                n -= 1
            else:
                nums1[last] = nums1[m]
                m -= 1

            last -= 1

        if n >= 0:
            nums1[: n + 1] = nums2[:n + 1]


# https://leetcode.com/problems/merge-intervals/
class Solution56:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            start1, end1 = res[-1]
            start2, end2 = intervals[i]

            if end1 < start2:
                res.append(intervals[i])
            else:
                res[-1][-1] = max(end2, end1)

        return res


# https://leetcode.com/problems/interval-list-intersections/
class Solution986:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        m, n = len(firstList), len(secondList)
        while i < m and j < n:
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            if start1 > end2:
                j += 1
            elif start2 > end1:
                i += 1
            else:
                min_start = max(start1, start2)
                min_end = min(end1, end2)
                res.append([min_start, min_end])
                if min_end == end1:
                    i += 1
                else:
                    j += 1

        return res
