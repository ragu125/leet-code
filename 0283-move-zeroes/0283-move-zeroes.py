class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        res=[]
        z=[]

        for i in nums:
            if i ==0:
                z.append(i)
            else:
                res.append(i)

        nums[:]=res+z
        return nums            