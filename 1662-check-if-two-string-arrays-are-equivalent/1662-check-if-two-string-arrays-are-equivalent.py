class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res=""
        for i in word1:
            res+=i
        sb=""
        for j in word2:
            sb+=j
        return res==sb        