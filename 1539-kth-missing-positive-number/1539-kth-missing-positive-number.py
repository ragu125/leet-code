from itertools import count
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res=[]

        for i in count(1):
            if i not in arr:
                res.append(i)
                if len(res)==k:
                    return res[-1]   
        