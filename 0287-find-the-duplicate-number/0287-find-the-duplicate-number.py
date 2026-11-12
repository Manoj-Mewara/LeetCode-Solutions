class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s1 = set()
        for i in nums:
            if i in s1:
                return i
            s1.add(i)