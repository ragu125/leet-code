from itertools import combinations_with_replacement
class Solution:
    def countVowelStrings(self, n: int) -> int:
        a=["a","e","i","o","u"]
        c=combinations_with_replacement(a,n)
        res=[]

        for i in c:
            res.append(i)

        return len(res)  