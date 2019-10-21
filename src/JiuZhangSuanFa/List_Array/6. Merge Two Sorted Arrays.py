class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here

        a, b = 0, 0
        res = []
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                res.append(A[a])
                a += 1
            else:
                res.append(B[b])
                b += 1

        if a >= len(A):
            for i in range(b, len(B)):
                res.append(B[i])
        else:
            for i in range(a, len(A)):
                res.append(A[i])

        return res