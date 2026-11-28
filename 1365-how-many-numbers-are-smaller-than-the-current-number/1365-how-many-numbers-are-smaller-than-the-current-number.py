class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        l = len(nums)
        l1 = []
        # count = 0 we can't use here, because for next number it would not be zero.
        
        for i in nums:
            count = 0       #For every new number, counting start from zero.
            for j in nums:
                if i > j:
                    count += 1
            l1.append(count)
        return l1

        # # We also can use this, because the number's index(it's previous numbers) is lowest than it. 
        # sorted_nums = sorted(nums)
        # l1 = []
        # for i in nums:
        #     count = sorted_nums.index(i)
        #     l1.append(count)
        # return l1


