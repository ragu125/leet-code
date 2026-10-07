class Solution:
    def check(self, nums: list[int]) -> bool:
        n=sorted(nums)
        a=nums+nums

        for i in range(len(nums)+1):
            if a[i:i+len(nums)]==n:
                return True
        return False          


