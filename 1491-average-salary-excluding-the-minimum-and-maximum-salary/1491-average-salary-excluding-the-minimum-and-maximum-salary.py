class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        res=[]
        for i in range(1,len(salary)-1):
            res.append(salary[i])
        p=len(res)
        return sum(res)/p