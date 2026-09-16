class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs=list(zip(heights,names))
        pairs=sorted(pairs,reverse=True)

        res=[]

        for height,name in pairs:
            res.append(name)

        return res    