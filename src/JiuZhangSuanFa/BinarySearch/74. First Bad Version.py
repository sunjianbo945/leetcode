# class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
# class Solution:
#     """
#     @param n: An integer
#     @return: An integer which is the first bad version.
#     """
#
#     def findFirstBadVersion(self, n):
#         # write your code here
#         l = 0
#         r = n
#
#         while l + 1 < r:
#
#             mid = (l + r) // 2
#
#             if SVNRepo.isBadVersion(mid):
#                 r = mid
#             else:
#                 l = mid
#
#         if SVNRepo.isBadVersion(r):
#             return r
#
#         return l