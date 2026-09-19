class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**0.5)

        while a<=b:
            x=a*a+b*b
            if x==c:
                return True
            elif x<c:
                a+=1
            else:
                b-=1
        return False                