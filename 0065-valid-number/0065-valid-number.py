class Solution:
    def isNumber(self, s: str) -> bool:
        if s in ["inf","-inf","+inf","Infinity","-Infinity","NaN","+Infinity","nan"]:
            return False
        try:
            float(s)
            return True
        except:
            return False    
        