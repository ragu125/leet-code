from collections import Counter
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        c=Counter(nums)

        for i in c:
            if c[i]>=2:
                return i