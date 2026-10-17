from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        p=permutations(nums)
        res=[]
        for i in p:
            res.append(i)
        return res    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna