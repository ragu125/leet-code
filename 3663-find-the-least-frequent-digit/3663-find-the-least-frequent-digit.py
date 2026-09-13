from collections import Counter
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        c=Counter(str(n))
        res=[]
        m=min(c.values())
        for i in c:
            if c[i]==m:
                res.append(int(i))
        return min(res)        
