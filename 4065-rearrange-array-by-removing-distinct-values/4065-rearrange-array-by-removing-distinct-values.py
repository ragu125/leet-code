class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while nums:
            x=sorted(set(nums))
            ans.extend(x)
            for i in x:
                nums.remove(i)
        return ans        