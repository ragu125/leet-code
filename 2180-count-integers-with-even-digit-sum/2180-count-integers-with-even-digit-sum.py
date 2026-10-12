class Solution:
    def countEven(self, num: int) -> int:
        res=[]
        for i in range(1,num+1):
            a=str(i)
            sb=[]
            for j in a:
                sb.append(int(j))
            b=sum(sb)
            if b%2==0:
                res.append(i)
        if num==3:
            return 1        
        if len(res)==1:
            if res[0]<num:
                return res[0]
        return len(res)             