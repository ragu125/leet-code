class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res=""
        for i in nums:
            res+=str(i)
        sb=[]
        for j in res:
            if int(j)==digit:
                sb.append(j)
        return len(sb)