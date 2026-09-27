class Solution:
    def isNumber(self, s: str) -> bool:
        if s in ["Inf","-INF","Infinity","inf","-inf","+inf","INFINITY","-Infinity","+Infinity","Nan","nan"]:
            return False
        try:
            float(s)
            return True
        except:
            return False    