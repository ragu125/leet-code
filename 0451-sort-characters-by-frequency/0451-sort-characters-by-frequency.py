from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)

        res=""

        for ch,freq in c.most_common():
            res+=ch*freq

        return res    