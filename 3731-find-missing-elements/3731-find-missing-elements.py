class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        a=nums[0]
        b=nums[-1]

        for i in range(a,b+1):
            if i not in nums:
                res.append(i)
        return res        
