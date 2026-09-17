class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        res=sum(matrix,[])
        res.sort()
        return res[k-1]
        