class Solution:
    def countSubstrings(self, s: str) -> int:
        res=[]

        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                a=s[i:j]
                if a==a[::-1]:
                    res.append(a)
        return len(res)            