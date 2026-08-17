class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                x=s[i:j+1]

                if x==x[::-1] and len(x) >len(res):
                    res=x
        return res            
        