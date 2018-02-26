class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Given two arrays, write a function to compute their intersection.(find common elements)
        Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
        """
