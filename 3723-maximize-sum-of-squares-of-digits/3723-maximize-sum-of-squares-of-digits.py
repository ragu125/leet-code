class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>num*9:
            return ""
        res=""

        for i in range(num):
            d=min(9,sum)
            res+=str(d)
            sum-=d

        return res       