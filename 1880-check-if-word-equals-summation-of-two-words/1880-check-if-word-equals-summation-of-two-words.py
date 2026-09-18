class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f=int("".join(str(ord(c)-97) for c in firstWord))
        s=int("".join(str(ord(c)-97) for c in secondWord))
        t=int("".join(str(ord(c)-97) for c in targetWord))
        return f+s==t