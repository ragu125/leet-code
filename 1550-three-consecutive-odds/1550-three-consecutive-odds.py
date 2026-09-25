class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr)-2):
            j=i+1
            k=j+1
            if arr[i]%2==1 and arr[j]%2==1 and arr[k]%2==1:
                return True
        return False        