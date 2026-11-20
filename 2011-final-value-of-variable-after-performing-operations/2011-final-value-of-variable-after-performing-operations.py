class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        s = 0
        for i in operations:
            if i == "X++" or i == "++X":
                s = s + 1
            elif i == "X--" or i == "--X":
                s = s - 1
        return s
"""
Or short code:
    x = 0
        for i in operations:
            if "+" in i:
                x = x + 1
            else:
                x = x - 1
        return x
"""