from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=range(1,n+1)

        for i,p in enumerate(permutations(nums),1):
            if i==k:
                return "".join(map(str,p))