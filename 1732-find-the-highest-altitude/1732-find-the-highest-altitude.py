class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        a=0
        max_a=0
        for i in gain:
            a+=i
            max_a=max(a,max_a)

        return max_a    