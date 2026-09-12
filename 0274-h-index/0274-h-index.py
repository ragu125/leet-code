class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        h=0
        for i,x in  enumerate(citations):
            if x>=i+1:
                h+=1
            else:
                break
        return h            