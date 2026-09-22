class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total=sum(nums[:k])
        max_sum=total

        for i in range(k,len(nums)):
            total=total-nums[i-k]+nums[i]
            max_sum=max(total,max_sum)

        return max_sum/k    