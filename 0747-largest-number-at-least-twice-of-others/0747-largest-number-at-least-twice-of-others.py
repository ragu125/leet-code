class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        index=nums.index(m)

        for i in nums:
            if i!=m and m<i*2:
                return -1
        return index      