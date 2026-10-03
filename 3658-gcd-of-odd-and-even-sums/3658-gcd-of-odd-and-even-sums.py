from itertools import count
from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        res=[]
        sb=[]
        for i in count(1):
            if int(i)%2==0:
                res.append(i)
            else:
                sb.append(i)    
            if len(res)==n:
                break
        return gcd(sum(res),sum(sb))                

        