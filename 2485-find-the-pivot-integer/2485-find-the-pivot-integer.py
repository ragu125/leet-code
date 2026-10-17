class Solution:
    def pivotInteger(self, n: int) -> int:
        ts=(n*(n+1))//2

        x=math.isqrt(ts)
        if x*x==ts:
            return x
        return -1    