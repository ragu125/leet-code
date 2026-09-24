class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans=float('inf')

        while nums:
            a=(nums[0]+nums[-1])/2
            ans=min(ans,a)

            nums.pop()
            nums.pop(0)

        return ans    
