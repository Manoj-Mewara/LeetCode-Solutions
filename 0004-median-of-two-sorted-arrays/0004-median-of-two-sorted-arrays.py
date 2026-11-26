class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = sorted(nums1 + nums2)       #  Merge both arrays and sort them
        n = len(nums3)
        if n % 2 != 0:              # If total numbers are odd.the ans is half of middle number
            result = float(nums3[n // 2])
            return result
        else:               # If total numbers are even. the ans is avg. of 2 middle number
            result = (nums3[n // 2] + nums3[n // 2 - 1]) / 2
            return result
