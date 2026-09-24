from itertools import permutations
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        p=permutations(nums)

        res=[]

        for i in p:
            res.append(i)

        return list(set(res))    