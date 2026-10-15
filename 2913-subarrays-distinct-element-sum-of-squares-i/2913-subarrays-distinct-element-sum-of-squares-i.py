class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res=[]

        for i in range(len(nums)+1):
            for j in range(i+1,len(nums)+1):
                a=set(nums[i:j])
                res.append(len(a))
        sp=[]
        for k in res:
            sp.append(int(k)**2) 

        return sum(sp)      