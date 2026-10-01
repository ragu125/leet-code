class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        res=[]
        gp=[]
        for i in nums:
            sb=[]
            for j in str(i):
                sb.append(int(j))
            a=max(sb)
            b=min(sb)
            res.append(a-b)
        g=max(res)
        for l in range(len(res)):
            if res[l]==g:
                gp.append(nums[l])
        return sum(gp)        
