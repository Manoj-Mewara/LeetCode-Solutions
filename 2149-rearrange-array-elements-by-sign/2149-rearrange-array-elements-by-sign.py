class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pve = []
        nve = []
        for i in nums:
            if i > 0:
                pve.append(i)
            else:
                nve.append(i)
        ans = []
        for j in range(len(pve)):
            ans.append(pve[j])
            ans.append(nve[j])
        return ans
