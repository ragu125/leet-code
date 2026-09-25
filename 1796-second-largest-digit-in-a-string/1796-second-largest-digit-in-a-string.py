class Solution:
    def secondHighest(self, s: str) -> int:
        res=[]

        for i in s:
            if i.isdigit():
                res.append(int(i))
        a=list(sorted(set(res))) 
        if len(a)<2:
            return -1     
        return a[-2]            