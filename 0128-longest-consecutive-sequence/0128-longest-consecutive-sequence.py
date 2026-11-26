class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        l1 = sorted(set(nums))
        count = 1 
        longest = 1

        for i in range(1, len(l1)):
            
            if l1[i] - l1[i - 1] == 1:      # Check if they are consecutive or not
                count += 1
                if count > longest:
                    longest = count
            else:
                count = 1

        return longest

       


            
