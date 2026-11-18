class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        s1 = set()
        for i in accounts:
            s1.add(sum(i))
        
        return max(s1)