class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[]
        for i in set(nums1):
            if i not in nums2 and i not in res:
                res.append(i) 
        sb=[]
        for j in set(nums2):
            if j not in nums1:
                sb.append(j)
        return [res,sb]      
        