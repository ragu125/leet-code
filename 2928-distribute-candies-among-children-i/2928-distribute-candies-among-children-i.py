class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans=0

        for i in range(limit+1):
            for j in range(limit+1):
                c=n-i-j

                if 0<=c<=limit:
                    ans+=1
        return  ans            
