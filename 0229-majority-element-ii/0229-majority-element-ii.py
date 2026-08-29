from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)

        res=[]

        c=Counter(nums)
        for i in c:
            if c[i] > n // 3:
                res.append(i)

        return res        



        