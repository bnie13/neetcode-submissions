class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = {}
        tc = {}
        for c in s:
            sc[c] = sc.get(c, 0) + 1
        for c in t:
            tc[c] = tc.get(c,0) + 1
        return sc == tc

        