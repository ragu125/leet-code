class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]

        for i in nums:
            target=[]
            for j in res:
                a=j+[i]
                target.append(a)
            res+=target
        return res        