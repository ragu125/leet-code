class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        res=[]
        for i in s:
            if i == letter:
                res.append(i)
        n=len(res)
        return int(n/len(s)*100)     