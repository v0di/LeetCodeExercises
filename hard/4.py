# Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        size = len(nums)
        half = nums[(size-1)//2]
        if not size%2:
            return (half + nums[(size)//2])/2
        return half
