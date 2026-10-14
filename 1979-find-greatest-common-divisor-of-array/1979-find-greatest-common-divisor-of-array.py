from math import gcd
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        s=min(nums)
        m=max(nums)
        return gcd(s,m)