class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        s=sorted(set(arr))
        d={}

        for rank,val in enumerate(s):
            d[val]=rank+1

        res=[]

        for i in arr:
            res.append(d[i])

        return res        
