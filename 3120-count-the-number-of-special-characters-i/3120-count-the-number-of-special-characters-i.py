class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res=0

        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in word and i.upper() in word:
                res+=1

        return res       