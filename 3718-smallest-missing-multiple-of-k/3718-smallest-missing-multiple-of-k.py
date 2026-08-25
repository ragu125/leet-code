class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        res=[]

        i=1
        while i>0:
            a=i*k
            if a in nums:
                i+=1
            else:
                res.append(a)
                break

        return res[0]
