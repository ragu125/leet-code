from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        res=[]
        for i in c:
            if c[i]==1:
                res.append(i)
        return res        