class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        res=[""]*len(words)

        for word in words:
            pop=int(word[-1])
            res[pop-1]=word[:-1]
        return " ".join(res)    