from itertools import permutations
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        p=permutations(nums)
        res=[]
        for i in p:
            if i not in res:
                res.append(i)
        return res        