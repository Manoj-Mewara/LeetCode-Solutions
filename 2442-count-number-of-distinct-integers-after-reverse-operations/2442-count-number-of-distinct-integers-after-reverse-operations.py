class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        s1 = set(nums)
        for i in nums:
            reverse = int(str(i)[::-1])     # It will reverse all number. Convert str to int. 
            s1.add(reverse)                 # Add reverse number in set & duplicate will delete.
        return len(s1)                      # Only unique numbers remain in set. so Ans is len.