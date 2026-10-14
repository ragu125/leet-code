class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        res=""
        for i in str(n):
            if int(i)!=0:
                res+=str(i)
        sb=[]
        for j in res:
            sb.append(int(j))
        a=sum(sb)
        return int(res) * a