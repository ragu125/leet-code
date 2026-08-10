class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros=[]
        res=[]

        for i in nums:
            if i ==0:
                zeros.append(i)
            else:
                res.append(i)
        nums[:]=res+zeros
        return nums                        
       