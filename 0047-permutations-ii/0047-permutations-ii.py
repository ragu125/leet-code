from itertools import permutations
class Solution:
    def permuteUnique(self, nums:list[int]) -> list[list[int]]:
        res=[]
        p=permutations(nums)
        for i in p:
            res.append(i)
        sb=[]

        for j in res:
            if j not in sb:
                sb.append(j)
        return sb        