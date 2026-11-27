class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        l1 = []
        max1 = max(candies)
        for i in candies:
            if (i + extraCandies) >= max1:
                ans = True
            else:
                ans = False
            l1.append(ans)
        return l1