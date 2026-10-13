class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        s=sorted(arr)
        c=0
        arr1=0
        arr2=0
        for i in range(len(arr)):
            arr1+=arr[i]
            arr2+=s[i]

            if arr1==arr2:
                c+=1
        return c        