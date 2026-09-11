from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=Counter(nums)
        k=0

        for x in c:
            for _ in range(min(c[x],2)):
                nums[k]=x
                k+=1
        return k        
        