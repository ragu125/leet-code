from collections import Counter
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        c=Counter(nums)
        res=[]

        for i in c:
            if c[i]==1:
                res.append(i)
        return sum(res)        