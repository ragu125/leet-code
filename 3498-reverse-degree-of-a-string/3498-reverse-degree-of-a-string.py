class Solution:
    def reverseDegree(self, s: str) -> int:
        str="Azyxwvutsrqponmlkjihgfedcba"
        res=[]
        c=0
        for i in s:
            c+=1
            if i in str:
                a=str.index(i)*c
                res.append(a)
        return sum(res)         