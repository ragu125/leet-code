class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        res=[]

        for i in nums:
            if i!=val:
                res.append(i)
        nums[:]=res
        return len(nums)        