class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res=[]
        for i in range(len(arr)+1):
            for j in range(i+1,len(arr)+1):
                res.append(arr[i:j])
        sb=[]
        for k in res:
            if len(k)%2!=0:
                sb.append(sum(k))
        return sum(sb)            