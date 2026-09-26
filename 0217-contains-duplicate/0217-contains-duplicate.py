from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        c=Counter(nums)

        for i in c:
            if c[i]>1:
                return True
        return False        