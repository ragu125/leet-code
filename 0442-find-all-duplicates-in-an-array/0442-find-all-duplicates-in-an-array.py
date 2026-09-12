class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]

        for i in nums:
            x=abs(i)-1

            if nums[x]<0:
                ans.append(abs(i))
            else:
                nums[x]=-nums[x]
        return ans            
        