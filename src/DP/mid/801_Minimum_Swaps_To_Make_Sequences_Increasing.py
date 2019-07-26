from typing import List

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        #https://www.cnblogs.com/grandyang/p/9311385.html
         # too dificult to understand the problem
        # why there is minium swap
        # firstly, write a greedy method to get test case
        # count = 0
        # for i in range(1, len(A)):
        #     if A[i] > A[i-1] and B[i] > B[i-1]:
        #         continue
        #     else:
        #         A[i], B[i] = B[i], A[i]
        #         count += 1
        # return count
		# 75 / 102 test cases passed.
		# bad case: [0,4,4,5,9] [0,1,6,8,10]
		# from this I know the situation when A[i] > A[i-1] and B[i] > B[i-1], ith can swap to get the minium.
		# then I figure out the following three situation we should care about
		# a、you must swap i th ele between A and B
		# b、you can swap or keep i th
		# c、you should keep  i th
        keep = [0 for _ in range(len(A))]
        swap = [0 for _ in range(len(A))]
        keep[0], swap[0] = 0, 1
        for i in range(1, len(A)):
            # must swap
            if A[i] <= A[i-1] or B[i] <= B[i-1]:
                swap[i] = keep[i-1] + 1
                keep[i] = swap[i-1]
            # swap or keep, both are ok
            elif A[i] > B[i-1] and B[i] > A[i-1]:
                swap[i] = min(swap[i-1], keep[i-1]) + 1
                keep[i] = min(keep[i-1], swap[i-1])
            # must keep
            else:
                swap[i] = swap[i-1] + 1
                keep[i] = keep[i-1]
        return min(swap[len(A)-1], keep[len(A)-1])

def main():
    print(Solution().minSwap([1,3,5,4],[1,2,3,7]))


if __name__=='__main__':
    main()
