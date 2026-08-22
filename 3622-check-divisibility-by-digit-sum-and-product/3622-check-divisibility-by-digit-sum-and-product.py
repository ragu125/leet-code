from math import prod
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        res=[]
        for i in str(n):
            res.append(int(i))
        ab=sum(res)
        sb=prod(res)
        k=ab+sb
        return n%(k)==0




            
        