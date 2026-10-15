class Solution:
    def longestDecomposition(self, text: str) -> int:
        res=0
        l=""
        r=""
        i=0
        j=len(text)-1

        while i<=j:
            l+=text[i]
            r=text[j]+r

            if l==r:
                res+=2 if i!=j else 1
                l=""
                r=""
            i+=1
            j-=1    
        if l:
            res+=1    

        return res    