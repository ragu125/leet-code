class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res=[]
        for i in order:
            for j in s:
                if i==j:
                    res.append(i)
        for j in s:
            if j not in order:
                res.append(j)
        return "".join(res)           