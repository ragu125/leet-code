class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res=[]

        for i in stones:
            if i in jewels:
                res.append(i)
        return len(res)        
        