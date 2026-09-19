class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res=0
        sb=0
        for i in nums:
            if i ==0:
                if res<sb:
                    res=sb
                sb=0
            else:
                sb+=1
        if res<sb:
            res=sb        
        return res                

