class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s1 = set()
        for i in nums:
            if i in s1:
                return True
            s1.add(i)
        else:
            return False