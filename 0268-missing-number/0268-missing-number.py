class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s1 = set(nums)
        for i in range(len(nums) + 1):
            if i not in s1:
                return i