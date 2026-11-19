class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s = 0
        l1 = []
        for i in nums:
            s = s + i
            l1.append(s)
        return l1
