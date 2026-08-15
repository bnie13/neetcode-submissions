class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = {}
        tc = {}
        for char in s:
            sc[char] = sc.get(char, 0) + 1
        for char in t:
            tc[char] = tc.get(char, 0) + 1
        if sc == tc:
            return True
        return False
        