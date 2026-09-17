from math import gcd
class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        g=0
        for i in nums:
            g=gcd(g,i)

        return g==1    
        