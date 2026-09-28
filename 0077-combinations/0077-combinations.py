from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        sb=[]

        for i in range(1,n+1):
            sb.append(i)
        c=combinations(sb,k)
        res=[]

        for j in c:
            res.append(j)
        return res        