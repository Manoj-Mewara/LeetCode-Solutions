class Solution:
    def removeStars(self, s: str) -> str:
        l1 = []
        for i in s:
            if i == "*":
                l1.pop()        # The last number will appear before the star(*).
            else:
                l1.append(i)    # Append the alphabets one by one to an empty list.
        return "".join(l1)      # The join method joins list items into a single string.