from itertools import count
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in count(0):
            if i not in nums:
                return i