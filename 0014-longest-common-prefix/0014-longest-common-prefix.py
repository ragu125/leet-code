class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pr=strs[0]

        for i in strs[1:]:
            while not i.startswith(pr):
                pr=pr[:-1]

        return pr        