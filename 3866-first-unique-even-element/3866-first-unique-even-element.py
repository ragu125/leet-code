from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        c=Counter(nums)
        for i in c:
            if c[i]==1:
                if i%2==0:
                    return i
        return -1            