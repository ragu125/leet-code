class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=""
        c=0
        for i in s:
            if i==" ":
                res+=i
                c+=1
                if c==k:
                    break
            else:
                res+=i  
        if res[-1]==" ":
            res=res[:-1]             
        return res             