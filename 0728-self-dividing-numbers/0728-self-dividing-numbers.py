class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            valid=True
            for j in str(i):
                if j =="0" or i%int(j)!=0:
                    valid=False
                    break
            if valid:
                ans.append(i)
        return ans            
