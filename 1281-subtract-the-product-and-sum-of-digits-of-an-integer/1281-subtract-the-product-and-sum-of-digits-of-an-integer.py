from math import prod
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        res=[]
        for i in n:
            res.append(int(i))
        a=prod(res)
        b=sum(res)   
        return a-b 