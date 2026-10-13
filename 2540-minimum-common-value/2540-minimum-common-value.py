class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        s=set(nums1)
        for i in nums2:
            if i in s:
                return i
        return -1        