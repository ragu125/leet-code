class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res=[]
        for i in range(len(arr2)):
            for j in arr1:
                if arr2[i]==j:
                    res.append(j)
        for j in sorted(arr1):
            if j not in arr2:
                res.append(j)        
        return res            