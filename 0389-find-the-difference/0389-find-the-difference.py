class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=[]
        for i in t:
            if t.count(i)!=s.count(i):
                return i