class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        last = len(A) - 1
        while m > 0 and n > 0:

            if A[m - 1] > B[n - 1]:
                A[last], A[m - 1] = A[m - 1], A[last]
                m -= 1
            else:
                A[last] = B[n - 1]
                n -= 1

            last -= 1

        if n > 0:
            for i in range(n):
                A[i] = B[i]

        return A