class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
            else:       # If you don't use else yet your code runs successfully.
                pass
        return count