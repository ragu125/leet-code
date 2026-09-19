class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=[]
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                res.append(i)
        return res        