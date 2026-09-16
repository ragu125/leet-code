from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=Counter(words[0])

        for words in words[1:]:
            common&=Counter(words)

        res=[]

        for ch in common:
            for _ in range(common[ch]):
                res.append(ch)
        return res        