class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res=""

        for i in nums:
            res+=str(i)
        sb=[]

        for j in res:
            sb.append(int(j))
        return sb    