from math import gcd
from math import lcm
from functools import reduce
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)    

        for i in range(n):
            res=nums[:i]+nums[i+1:]

            if not res:
                g=nums[0]
                l=nums[0]
            else:
                g=reduce(gcd,res)
                l=reduce(lcm,res) 
            ans=max(ans,g*l) 

        g=reduce(gcd,nums)
        l=reduce(lcm,nums) 

        return max(ans,g*l)             
