from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        for i in range(1,n+1):
            res.append(i)
        c=combinations(res,k)
        sb=[]
        for j in c:
            sb.append(j)
        return sb        