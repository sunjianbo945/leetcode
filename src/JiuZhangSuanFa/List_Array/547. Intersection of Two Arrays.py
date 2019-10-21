class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        has1 = set(nums1)
        has2 = set(nums2)
        return list(has1.intersection(has2))