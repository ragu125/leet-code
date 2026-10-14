class Solution:
    def processStr(self, s: str) -> str:
        alp="abcdefghijklmnopqrstuvwxyz"
        res=""
        for i in s:
            if i=="#":
                res*=2
            elif i=="*":
                res=res[:-1]
            elif i=="%":
                res=res[::-1]
            else:
                res+=i
        sb=""
        for j in res:
            if j in alp:
                sb+=j
        return sb                   